from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)


def test_ffmpeg_renderer_builds_concat_filter():

    renderer = FFmpegRenderer(
        AssetRegistry()
    )

    result = renderer.build_concat_filter(
        2
    )

    assert result == (
        "[0:v][1:v]concat=n=2:v=1:a=0[out]"
    )
