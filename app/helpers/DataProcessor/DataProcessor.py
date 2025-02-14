import re

from app.helpers.GenerativeAIManager import AnthropicResource
from .conf import PATTERNS, PATTERNS_QUESTIONS
from typing import Optional


class DataProcessor():
    _ai_resource: Optional[AnthropicResource]
    _data: dict
    _processed_data: dict

    def __init__(self, data: dict, ai_manager: Optional[AnthropicResource] = None) -> None:
        self._data = data
        self._processed_data = {}
        self._ai_resource = ai_manager

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
                    pattern_values.append([
                        {
                            "name": pat["name"],
                            "value": get_value(pat["value"]),
                        } for pat in pattern
                    ])
                elif isinstance(pattern, dict):
                    pattern_values = search_from_patterns(pattern)

                processed_data[pattern_key] = pattern_values[0] if isinstance(pattern, list) and len(pattern_values) == 1 else pattern_values
            return processed_data

        self._processed_data = search_from_patterns(PATTERNS)

    def get_ai_data(self):

        def get_or_set_value(pattern_keys: dict, value = None):
            *path_keys, last_key = pattern_keys.split(".")
            last_key = int(last_key) if last_key.isdigit() else last_key

            current_dict = self._processed_data
            for path_key in path_keys:
                current_dict = current_dict.get(path_key, {})

            if value == None:
                return current_dict[last_key] if isinstance(current_dict, list) else current_dict.get(last_key)

            if isinstance(current_dict[last_key], dict):
                current_dict[last_key]["value"] = value
            else:
                current_dict[last_key] = value

        def get_answers_from_ai() -> dict:
            content = ""
            content += "You are an expert in Medicine and Health Insurance."
            content += "You will receive information_key, information_value and then information_question."
            for pattern_keys, question in PATTERNS_QUESTIONS.items():
                content += f"<information_key>{pattern_keys}</information_key>"
                content += f"<information_value>{get_or_set_value(pattern_keys)}</information_value>"
                content += f"<information_question>{question}</information_question>"

            content += """
            Please return the response using the following pattern, noting that "information_result" is the answer to each question:
            <response>{
                "information_key_1": "information_result about information_key_1",
                "information_key_2": "information_result about information_key_2",
                ...
            }
            </response>"""

            # messages = self._ai_resource.get_answers(content)
            messages = {
                "requirements.0": True,
                "requirements.2": True,
                "requirements.3": "Data Not Available",
                "benefits.1": "0.00",
                "details.eligibility": "Patient must have commercial insurance and be a legal US resident, excluding those with Medicaid, Medicare, VA, DOD, TRICARE, or other federal/state programs.",
                "details.program": "The patient is under the Dupixent MyWay Copay Card Program.",
                "details.renewal": "Patient will be automatically re-enrolled every January 1st if their card has been used within 18 months."
            }
            return messages

        def get_answers_from_code() -> dict:
            messages = {
                "details.income": "",
                "funding.evergreen": "",
                "funding.current_funding_level": "",
            }

            for key, value in messages.items():
                messages[key] = get_or_set_value(pattern_keys=key)

            messages["details.income"] = "Not required" if messages["details.income"][0] == False else messages["details.income"][1]
            messages["funding.evergreen"] = True if messages["funding.evergreen"][0] == None else messages["funding.evergreen"][1]
            messages["funding.current_funding_level"] = "Data Not Available" if messages["funding.current_funding_level"][0] == None else messages["funding.current_funding_level"][1]

            return messages

        messages_to_replace = {}
        messages_to_replace.update(get_answers_from_code())
        messages_to_replace.update(get_answers_from_ai())

        for pattern_keys, question_answered in messages_to_replace.items():
            get_or_set_value(
                pattern_keys=pattern_keys,
                value=question_answered
            )

