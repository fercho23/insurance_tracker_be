# tests/test_generative_ai_constructor.py
import pytest
from app.helpers.GenerativeAIManager import GenerativeAIConstructor
from app.helpers.GenerativeAIManager.resources import AnthropicResource
from app.helpers.GenerativeAIManager.resources import ResourceInterface


@pytest.mark.unit
@pytest.mark.helpers
class TestGenerativeAIConstructor:
    """Tests for the GenerativeAIConstructor class."""

    def test_get_resource(self):
        resource_name = "claude"
        resource = GenerativeAIConstructor.get_resource(resource_name)
        assert isinstance(resource, AnthropicResource)
        assert isinstance(resource, ResourceInterface)

    def test_get_resource_not_implemented(self):
        resource_name = "unknown"
        with pytest.raises(NotImplementedError):
            GenerativeAIConstructor.get_resource(resource_name)
