from pathlib import Path

from vda.models.task_result import TaskResult
from vda.providers.video.base import BaseVideoProvider


class MockVideoProvider(BaseVideoProvider):
    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:
        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output.write_text(
            "mock video",
            encoding="utf-8",
        )

        return TaskResult(
            task_id="video-001",
            provider="mock-video",
            status="completed",
            progress=100,
            local_file=str(output),
        )
