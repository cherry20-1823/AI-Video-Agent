from vda.models.timeline import Timeline
from vda.renderers.base import BaseRenderer


class FFmpegRenderer(BaseRenderer):

    def build_command(
        self,
        timeline: Timeline,
        output_path: str,
    ) -> list[str]:
        return [
            "ffmpeg",
            "-y",
            output_path,
        ]

    def render(
        self,
        timeline: Timeline,
        output_path: str,
    ) -> str:
        self.build_command(
            timeline,
            output_path,
        )

        return output_path
