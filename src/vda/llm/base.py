from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def generate_plan(self, topic: str) -> dict:
        pass
