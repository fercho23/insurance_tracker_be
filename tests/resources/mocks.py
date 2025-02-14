from unittest.mock import MagicMock

# import pytest_mock
# import anthropic
import pytest
from app.helpers.GenerativeAIManager.resources import AnthropicResource


@pytest.fixture
def mock_anthropic_client():
    class MockAnthropicClient:
        def __init__(self):
            self.messages = MagicMock()
            self.messages.create.return_value = {"content": [{"text": "mock response"}]}

    return MockAnthropicClient()
    # return mocker.Mock(spec=anthropic.Anthropic)


@pytest.fixture
def anthropic_resource(mock_anthropic_client):
    resource = AnthropicResource()
    resource._client = mock_anthropic_client
    return resource
