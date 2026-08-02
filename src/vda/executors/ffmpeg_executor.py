import subprocess

from vda.models.render_result import (
    RenderResult,
)


class FFmpegExecutor:

    def run(
        self,
        command: list[str],
    ) -> RenderResult:

        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )

        return RenderResult(
            success=(
                result.returncode == 0
            ),
            return_code=result.returncode,
            error=(
                result.stderr
                if result.returncode != 0
                else None
            ),
        )
