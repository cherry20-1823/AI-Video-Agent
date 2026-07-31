from pathlib import Path

from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider


class MockImageProvider(BaseImageProvider):

    @property
    def name(self) -> str:
        return "mock-image"

    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:

        Path(output_path).write_text(
            "Mock Image Generated\n\n" + prompt,
            encoding="utf-8",
        )

        return TaskResult(
            task_id="image-001",
            provider=self.name,
            status="completed",
            progress=100,
            local_file=output_path,
        )
