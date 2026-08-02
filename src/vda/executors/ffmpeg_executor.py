import subprocess


class FFmpegExecutor:

    def run(
        self,
        command: list[str],
    ) -> int:
        result = subprocess.run(
            command,
            check=False,
        )

        return result.returncode
