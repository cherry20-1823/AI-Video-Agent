from pathlib import Path

from vda.models.asset import (
    Asset,
)
from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.enums import (
    AssetType,
)
from vda.models.timeline import (
    Timeline,
)
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)


class MockExecutor:

    def __init__(self):
        self.command = None

    def run(
        self,
        command,
    ):
        self.command = command
        return 0


def test_ffmpeg_renderer_executes_command():

    registry = AssetRegistry()

    registry.add(
        Asset(
            id="video:scene-001",
            name="Scene 1",
            type=AssetType.VIDEO,
            path=Path(
                "scene-001/video.mp4"
            ),
        )
    )

    executor = MockExecutor()

    renderer = FFmpegRenderer(
        registry,
        executor,
    )

    result = renderer.render(
        Timeline(
            tracks=[]
        ),
        "movie.mp4",
    )

    assert result == "movie.mp4"

    assert executor.command is not None
