from abc import ABC, abstractmethod
from pathlib import Path

from vda.models.task_result import (
    TaskResult,
)


class BaseVideoProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:
        """Generate a video."""

    @abstractmethod
    def download(
        self,
        task: TaskResult,
    ) -> Path:
        """Download generated video."""
