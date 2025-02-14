import pytest

# from app.helpers.GenerativeAIManager.resources import AnthropicResource
from app.helpers.GenerativeAIManager.resources.AnthropicResource import (
    ANTHROPIC_MAX_TOKENS,
)
from app.helpers.GenerativeAIManager.resources.AnthropicResource import ANTHROPIC_MODEL


@pytest.mark.unit
@pytest.mark.helpers
@pytest.mark.skip("Mocking AnthropicClient is not working.")
class TestAnthropicResource:
    """Tests for the AnthropicResource class."""

    def test_get_answers(self, anthropic_resource, mock_anthropic_client):
        content = "test content"
        system = "test system"
        anthropic_resource.get_answers(content, system)
        mock_anthropic_client.messages.create.assert_called_once_with(
            model=ANTHROPIC_MODEL,
            max_tokens=ANTHROPIC_MAX_TOKENS,
            temperature=0,
            messages=[{"role": "user", "content": content}],
        )

    def test_process_response(self, anthropic_resource, mock_anthropic_client):
        message = {"content": [{"text": "<response>test response</response>"}]}
        mock_anthropic_client.messages.create.return_value = message
        response = anthropic_resource.get_answers("test content")
        assert response == {"text": "test response"}

    def test_process_response_invalid_message(
        self, anthropic_resource, mock_anthropic_client
    ):
        message = {"invalid": "message"}
        mock_anthropic_client.messages.create.return_value = message
        with pytest.raises(KeyError):
            anthropic_resource.get_answers("test content")
