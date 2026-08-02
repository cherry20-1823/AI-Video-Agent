from vda.models.timeline import (
    Segment,
    Timeline,
    Track,
    TrackType,
)


def test_timeline_creates_video_track():
    segment = Segment(
        asset_id="video:scene-001",
        start=0,
        duration=7,
    )

    track = Track(
        type=TrackType.VIDEO,
        segments=[segment],
    )

    timeline = Timeline(
        tracks=[track],
    )

    assert timeline.tracks[0].type == (
        TrackType.VIDEO
    )

    assert timeline.tracks[0].segments[0] == (
        segment
    )
