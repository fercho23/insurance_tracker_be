import re
from typing import Optional

from app.helpers.GenerativeAIManager import GenerativeAIConstructor
from app.helpers.GenerativeAIManager import ResourceInterface
from app.models import Company

from .conf import PATTERNS
from .conf import PATTERNS_QUESTIONS


class DataProcessor:
    _ai_resource: Optional[ResourceInterface]
    _data: dict
    _processed_data: dict

    def __init__(
        self, data: dict, ai_manager: Optional[ResourceInterface] = None
    ) -> None:
        self._data = data
        self._processed_data = {}
        self._ai_resource = ai_manager

    @staticmethod
    def create_by_company(data: dict, company: Company):
        return DataProcessor(
            data=data,
            ai_manager=GenerativeAIConstructor.get_resource(company.ai_resource),
        )

    def process(self) -> dict:
        self.get_simple_data()

        if self._ai_resource:
            self.get_ai_data()

        return self._processed_data

    def get_simple_data(self):
        def get_value(pattern_to_search: str):
            for key, value in self._data.items():
                if re.search(pattern_to_search, key):
                    return value
            return None

        def search_from_patterns(patterns: dict) -> dict:
            processed_data = {}
            for pattern_key, pattern in patterns.items():
                pattern_values = []
                if isinstance(pattern, str):
                    pattern_values.append(get_value(pattern))
                elif isinstance(pattern, tuple):
                    for pat in pattern:
                        pattern_values.append(get_value(pat))
                elif isinstance(pattern, list):
                    pattern_values.append(
                        [
                            {
                                "name": pat["name"],
                                "value": get_value(pat["value"]),
                            }
                            for pat in pattern
                        ]
                    )
                elif isinstance(pattern, dict):
                    pattern_values = search_from_patterns(pattern)

                processed_data[pattern_key] = (
                    pattern_values[0]
                    if isinstance(pattern, list) and len(pattern_values) == 1
                    else pattern_values
                )
            return processed_data

        self._processed_data = search_from_patterns(PATTERNS)

    def get_ai_data(self):
        def get_or_set_value(pattern_keys: dict, value=None):
            *path_keys, last_key = pattern_keys.split(".")
            last_key = int(last_key) if last_key.isdigit() else last_key

            current_dict = self._processed_data
            for path_key in path_keys:
                current_dict = current_dict.get(path_key, {})

            if value is None:
                return (
                    current_dict[last_key]
                    if isinstance(current_dict, list)
                    else current_dict.get(last_key)
                )

            if isinstance(current_dict[last_key], dict):
                current_dict[last_key]["value"] = value
            else:
                current_dict[last_key] = value

        def get_answers_from_ai() -> dict:
            # flake8: noqa: E501
            content = ""
            content += "You are an expert in Medicine and Health Insurance."
            content += "You will receive information_key, information_value and then information_question."
            for pattern_keys, question in PATTERNS_QUESTIONS.items():
                content += f"<information_key>{pattern_keys}</information_key>"
                content += f"<information_value>{get_or_set_value(pattern_keys)}</information_value>"
                content += f"<information_question>{question}</information_question>"

            content += """
            Please return the response using the following pattern,
            noting that "information_result" is the answer to each question:
            <response>{
                "information_key_1": "information_result about information_key_1",
                "information_key_2": "information_result about information_key_2",
                ...
            }
            </response>"""

            messages = self._ai_resource.get_answers(content)
            return messages

        def get_answers_from_code() -> dict:
            messages = {
                "details.income": "",
                "funding.evergreen": "",
                "funding.current_funding_level": "",
            }

            for key, _ in messages.items():
                messages[key] = get_or_set_value(pattern_keys=key)

            messages["details.income"] = (
                messages["details.income"][1]
                if not messages["details.income"][0]
                else "Not required"
            )
            messages["funding.evergreen"] = (
                True
                if messages["funding.evergreen"][0] is None
                else messages["funding.evergreen"][1]
            )
            messages["funding.current_funding_level"] = (
                "Data Not Available"
                if messages["funding.current_funding_level"][0] is None
                else messages["funding.current_funding_level"][1]
            )

            return messages

        messages_to_replace = {}
        messages_to_replace.update(get_answers_from_code())
        messages_to_replace.update(get_answers_from_ai())

        for pattern_keys, question_answered in messages_to_replace.items():
            get_or_set_value(pattern_keys=pattern_keys, value=question_answered)
