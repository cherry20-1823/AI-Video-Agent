from vda.models.timeline import (
    Timeline,
)
from vda.services.composer import (
    Composer,
)
from vda.workflow.render_workflow import (
    RenderWorkflow,
)


def test_render_workflow_returns_task_result():

    result = RenderWorkflow(
        Composer()
    ).run(
        "task-001",
        Timeline(
            tracks=[]
        ),
        "movie.mp4",
    )

    assert result.task_id == (
        "task-001"
    )

    assert result.status == (
        "completed"
    )

    assert result.local_file == (
        "movie.mp4"
    )
