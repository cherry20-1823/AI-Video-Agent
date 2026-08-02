
from vda.models.asset_registry import AssetRegistry
from vda.models.context import (
    PipelineContext,
)
from vda.models.enums import AssetType
from vda.models.project import (
    Project,
)
from vda.providers.video.mock.provider import (
    MockVideoProvider,
)
from vda.services.video_generator import (
    VideoGenerator,
)
from vda.storage.workspace import Workspace


def test_video_generator_creates_video_asset(
    tmp_path,
):
    workspace = Workspace(
        root=str(tmp_path)
    )

    registry = AssetRegistry()

    context = PipelineContext(
        topic="test",
        project=Project(
            id="project-001",
            title="test",
            description="",
            duration=60,
            aspect_ratio="16:9",
        ),
        workspace=workspace,
        asset_registry=registry,
    )

    generator = VideoGenerator(
        video_provider=MockVideoProvider(),
        context=context,
    )

    result = generator.generate(
        project_id="project-001",
        scene_id=1,
        prompt="future AI city",
    )

    assert result.status == "completed"

    assert (
        workspace.video_path(
            "project-001",
            1,
        ).exists()
    )

    videos = registry.by_type(
        AssetType.VIDEO
    )

    assert len(videos) == 1

    assert videos[0].id == (
        "video:scene-001"
    )

    assert videos[0].path == (
        workspace.video_path(
            "project-001",
            1,
        )
    )
