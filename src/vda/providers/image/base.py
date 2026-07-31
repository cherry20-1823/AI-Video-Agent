from abc import ABC, abstractmethod

from vda.models.task_result import TaskResult


class BaseImageProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:
        pass
