from unittest.mock import patch

from vda.executors.ffmpeg_executor import (
    FFmpegExecutor,
)


def test_ffmpeg_executor_returns_failure():

    with patch(
        "subprocess.run"
    ) as run:

        run.return_value.returncode = 1
        run.return_value.stderr = (
            "ffmpeg failed"
        )

        result = FFmpegExecutor().run(
            [
                "ffmpeg",
            ]
        )

    assert result.success is False

    assert result.return_code == 1

    assert result.error == (
        "ffmpeg failed"
    )
