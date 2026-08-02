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
    Segment,
    Timeline,
    Track,
    TrackType,
)
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)


def test_ffmpeg_renderer_builds_concat_command():

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

    registry.add(
        Asset(
            id="video:scene-002",
            name="Scene 2",
            type=AssetType.VIDEO,
            path=Path(
                "scene-002/video.mp4"
            ),
        )
    )

    timeline = Timeline(
        tracks=[
            Track(
                type=TrackType.VIDEO,
                segments=[
                    Segment(
                        asset_id="video:scene-001",
                        start=0,
                        duration=5,
                    ),
                    Segment(
                        asset_id="video:scene-002",
                        start=5,
                        duration=5,
                    ),
                ],
            )
        ]
    )

    command = FFmpegRenderer(
        registry
    ).build_command(
        timeline,
        "movie.mp4",
    )

    assert "-filter_complex" in command

    assert (
        "[0:v][1:v]concat=n=2:v=1:a=0[out]"
        in command
    )

    assert "-map" in command

    assert "[out]" in command
