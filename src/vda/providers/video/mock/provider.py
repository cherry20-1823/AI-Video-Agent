from pathlib import Path

from vda.models.task_result import (
    TaskResult,
)
from vda.providers.video.base import (
    BaseVideoProvider,
)


class MockVideoProvider(
    BaseVideoProvider
):

    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            "mock video",
            encoding="utf-8",
        )

        return TaskResult(
            task_id="mock-video-task",
            provider="mock-video",
            status="completed",
            local_file=str(path),
        )

    def download(
        self,
        task: TaskResult,
    ) -> Path:

        if task.local_file is None:
            raise RuntimeError(
                "No local file available"
            )

        return Path(
            task.local_file
        )
