from abc import ABC
from abc import abstractmethod


class ResourceInterface(ABC):
    @abstractmethod
    def get_answers(self, content: object, system: str):
        raise NotImplementedError()
