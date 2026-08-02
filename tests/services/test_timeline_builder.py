from pathlib import Path

from vda.models.asset import Asset
from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.enums import AssetType
from vda.services.timeline_builder import (
    TimelineBuilder,
)


def test_timeline_builder_builds_video_timeline():

    registry = AssetRegistry()

    registry.add(
        Asset(
            id="video:scene-001",
            name="Scene 1 Video",
            type=AssetType.VIDEO,
            path=Path(
                "scene-001/video.mp4"
            ),
            duration=7,
        )
    )

    registry.add(
        Asset(
            id="video:scene-002",
            name="Scene 2 Video",
            type=AssetType.VIDEO,
            path=Path(
                "scene-002/video.mp4"
            ),
            duration=5,
        )
    )

    timeline = TimelineBuilder().build(
        registry
    )

    segments = (
        timeline.tracks[0]
        .segments
    )

    assert len(segments) == 2

    assert segments[0].asset_id == (
        "video:scene-001"
    )

    assert segments[0].start == 0

    assert segments[1].start == 7


def test_timeline_builder_handles_empty_registry():

    registry = AssetRegistry()

    timeline = TimelineBuilder().build(
        registry
    )

    assert len(
        timeline.tracks
    ) == 1

    assert (
        timeline.tracks[0].segments
        == []
    )


def test_timeline_builder_creates_continuous_timeline():

    registry = AssetRegistry()

    registry.add(
        Asset(
            id="video:scene-001",
            name="Scene 1",
            type=AssetType.VIDEO,
            path=Path(
                "scene-001/video.mp4"
            ),
            duration=3,
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
            duration=4,
        )
    )

    timeline = TimelineBuilder().build(
        registry
    )

    segments = (
        timeline.tracks[0]
        .segments
    )

    assert segments[0].start == 0
    assert segments[0].duration == 3

    assert segments[1].start == 3
    assert segments[1].duration == 4
