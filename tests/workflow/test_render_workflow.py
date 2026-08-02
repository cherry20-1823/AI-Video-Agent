from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.context import (
    PipelineContext,
)
from vda.models.project import (
    Project,
)
from vda.models.timeline import (
    Timeline,
)
from vda.services.composer import (
    Composer,
)
from vda.storage.workspace import (
    Workspace,
)
from vda.workflow.render_workflow import (
    RenderWorkflow,
)


def test_render_workflow_returns_task_result():

    context = PipelineContext(
        topic="test",
        project=Project(
            id="project-001",
            title="test",
            description="",
            duration=60,
            aspect_ratio="16:9",
        ),
        workspace=Workspace(),
        asset_registry=AssetRegistry(),
    )

    result = RenderWorkflow(
        context,
        Composer(),
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
