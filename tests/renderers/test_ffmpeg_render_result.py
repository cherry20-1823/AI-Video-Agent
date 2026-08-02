from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.render_result import (
    RenderResult,
)
from vda.models.timeline import (
    Timeline,
)
from vda.renderers.ffmpeg import (
    FFmpegRenderer,
)


class SuccessExecutor:

    def run(
        self,
        command,
    ):
        return RenderResult(
            success=True,
            return_code=0,
        )


class FailedExecutor:

    def run(
        self,
        command,
    ):
        return RenderResult(
            success=False,
            return_code=1,
            error="ffmpeg failed",
        )


def test_renderer_returns_success_result():

    result = FFmpegRenderer(
        AssetRegistry(),
        SuccessExecutor(),
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


def test_renderer_returns_failure_result():

    result = FFmpegRenderer(
        AssetRegistry(),
        FailedExecutor(),
    ).render(
        Timeline(
            tracks=[]
        ),
        "movie.mp4",
    )

    assert result.success is False

    assert result.error == (
        "ffmpeg failed"
    )
