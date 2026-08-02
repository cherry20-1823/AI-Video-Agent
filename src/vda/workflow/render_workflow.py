from vda.models.task_result import (
    TaskResult,
)
from vda.models.timeline import (
    Timeline,
)
from vda.services.composer import (
    Composer,
)


class RenderWorkflow:

    def __init__(
        self,
        composer: Composer,
    ):
        self.composer = composer

    def run(
        self,
        task_id: str,
        timeline: Timeline,
        output_path: str,
    ) -> TaskResult:

        result = self.composer.compose(
            timeline,
            output_path,
        )

        if result.status != "completed":
            return TaskResult(
                task_id=task_id,
                provider="ffmpeg",
                status="failed",
            )

        return TaskResult(
            task_id=task_id,
            provider="ffmpeg",
            status="completed",
            local_file=result.output_path,
        )
