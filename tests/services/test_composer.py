from vda.models.timeline import (
    Segment,
    Timeline,
    Track,
    TrackType,
)
from vda.services.composer import (
    Composer,
)


def test_composer_returns_duration():

    timeline = Timeline(
        tracks=[
            Track(
                type=TrackType.VIDEO,
                segments=[
                    Segment(
                        asset_id="video:scene-001",
                        start=0,
                        duration=7,
                    ),
                    Segment(
                        asset_id="video:scene-002",
                        start=7,
                        duration=5,
                    ),
                ],
            )
        ]
    )

    result = Composer().compose(
        timeline
    )

    assert result.status == (
        "completed"
    )

    assert result.duration == 12
