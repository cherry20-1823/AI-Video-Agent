from pathlib import Path

from vda.models.asset import Asset
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType
from vda.models.timeline import (
    Segment,
    Timeline,
    Track,
    TrackType,
)
from vda.renderers.ffmpeg import FFmpegRenderer


def test_ffmpeg_renderer_maps_assets():

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

    timeline = Timeline(
        tracks=[
            Track(
                type=TrackType.VIDEO,
                segments=[
                    Segment(
                        asset_id="video:scene-001",
                        start=0,
                        duration=5,
                    )
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

    assert command == [
        "ffmpeg",
        "-y",
        "-i",
        "scene-001/video.mp4",
        "movie.mp4",
    ]
