from .resources import AnthropicResource
from .resources import ResourceInterface

RESOURCES_AVAILABLE = {"claude": AnthropicResource}


class GenerativeAIConstructor:
    @staticmethod
    def get_resource(resource_name: str) -> ResourceInterface:
        if resource_name in RESOURCES_AVAILABLE:
            return RESOURCES_AVAILABLE[resource_name]()
        raise NotImplementedError()
