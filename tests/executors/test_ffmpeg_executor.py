from unittest.mock import patch

from vda.executors.ffmpeg_executor import (
    FFmpegExecutor,
)


def test_ffmpeg_executor_returns_success():

    with patch(
        "subprocess.run"
    ) as run:

        run.return_value.returncode = 0

        result = FFmpegExecutor().run(
            [
                "ffmpeg",
                "-version",
            ]
        )

    assert result.success is True

    assert result.return_code == 0

    run.assert_called_once()
