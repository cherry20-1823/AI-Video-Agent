
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType
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

    generator = VideoGenerator(
        video_provider=MockVideoProvider(),
        workspace=workspace,
        registry=registry,
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
