from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.task_result import (
    TaskResult,
)
from vda.services.video_pipeline import (
    VideoPipeline,
)


class MockTimelineBuilder:

    def build(
        self,
        registry,
    ):
        return "timeline"


class MockRenderWorkflow:

    def run(
        self,
        task_id,
        timeline,
        output_path,
    ):
        return TaskResult(
            task_id=task_id,
            provider="ffmpeg",
            status="completed",
            local_file=output_path,
        )


def test_video_pipeline_runs():

    result = VideoPipeline(
        MockTimelineBuilder(),
        MockRenderWorkflow(),
    ).run(
        "task-001",
        AssetRegistry(),
        "movie.mp4",
    )

    assert result.status == (
        "completed"
    )

    assert result.local_file == (
        "movie.mp4"
    )
