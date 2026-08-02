from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.timeline import Timeline
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)


def test_ffmpeg_renderer_builds_command():

    timeline = Timeline(
        tracks=[]
    )

    renderer = FFmpegRenderer(
        AssetRegistry()
    )

    command = renderer.build_command(
        timeline,
        "movie.mp4",
    )

    assert command == [
        "ffmpeg",
        "-y",
        "movie.mp4",
    ]


def test_ffmpeg_renderer_returns_output():

    result = FFmpegRenderer(
        AssetRegistry()
    ).render(
        Timeline(
            tracks=[]
        ),
        "movie.mp4",
    )

    assert result.success is True

    assert result.output_path == (
        "movie.mp4"
    )
