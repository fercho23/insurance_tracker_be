from abc import ABC

class ResourceInterface(ABC):

    def get_answers(self, content: object, system: str):
        raise NotImplementedError()