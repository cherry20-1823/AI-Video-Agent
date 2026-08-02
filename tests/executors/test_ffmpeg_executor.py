from unittest.mock import patch

from vda.executors.ffmpeg_executor import (
    FFmpegExecutor,
)


def test_ffmpeg_executor_returns_code():

    with patch(
        "subprocess.run"
    ) as run:

        run.return_value.returncode = 0

        code = FFmpegExecutor().run(
            [
                "ffmpeg",
                "-version",
            ]
        )

    assert code == 0

    run.assert_called_once()
