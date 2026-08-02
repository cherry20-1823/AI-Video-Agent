from vda.models.timeline import (
    Segment,
    Timeline,
    Track,
    TrackType,
)
from vda.renderers.mock import (
    MockRenderer,
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
        timeline,
        output_path="movie.mp4",
    )

    assert result.status == (
        "completed"
    )

    assert result.duration == 12

    assert result.output_path == (
        "movie.mp4"
    )


def test_composer_uses_renderer():

    timeline = Timeline(
        tracks=[]
    )

    result = Composer(
        renderer=MockRenderer(),
    ).compose(
        timeline,
        output_path="movie.mp4",
    )

    assert result.output_path == (
        "movie.mp4"
    )
