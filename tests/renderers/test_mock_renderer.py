from vda.models.timeline import Timeline
from vda.renderers.mock import MockRenderer


def test_mock_renderer_returns_output_path():

    timeline = Timeline(
        tracks=[]
    )

    output = MockRenderer().render(
        timeline,
        "movie.mp4",
    )

    assert output == "movie.mp4"
