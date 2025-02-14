import json
import os

import anthropic

from app import logger

from .ResourceInterface import ResourceInterface

ANTHROPIC_SYSTEM = (
    os.getenv("ANTHROPIC_SYSTEM") or "You are an expert in health and drug insurance."
)
ANTHROPIC_MAX_TOKENS = int(os.getenv("ANTHROPIC_MAX_TOKENS") or 1000)
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-3-5-sonnet-20241022"


class AnthropicResource(ResourceInterface):
    _client: object

    def __init__(self):
        self._client = anthropic.Anthropic()

    def get_answers(self, content: object, system: str = ANTHROPIC_SYSTEM):
        logger.info("Anthropic Client is being called")
        message = self._client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=ANTHROPIC_MAX_TOKENS,
            temperature=0,
            # system=system,
            messages=[{"role": "user", "content": content}],
        )

        return self._process_response(message)

    def _process_response(self, message):
        message = message.content[0]
        message = message.text
        message = message.replace("<response>", "")
        message = message.replace("</response>", "")
        message = json.loads(message)
        return message
