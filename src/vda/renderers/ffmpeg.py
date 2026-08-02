from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.timeline import (
    Timeline,
)
from vda.renderers.base import (
    BaseRenderer,
)


class FFmpegRenderer(BaseRenderer):

    def __init__(
        self,
        registry: AssetRegistry,
    ):
        self.registry = registry

    def build_concat_filter(
        self,
        count: int,
    ) -> str:

        inputs = "".join(
            [
                f"[{index}:v]"
                for index in range(count)
            ]
        )

        return (
            f"{inputs}"
            f"concat=n={count}:v=1:a=0"
            "[out]"
        )


    def build_command(
        self,
        timeline: Timeline,
        output_path: str,
    ) -> list[str]:

        command = [
            "ffmpeg",
            "-y",
        ]

        input_count = 0

        for track in timeline.tracks:
            for segment in track.segments:
                asset = self.registry.get(
                    segment.asset_id
                )

                if asset is not None:
                    command.extend(
                        [
                            "-i",
                            str(asset.path),
                        ]
                    )

                    input_count += 1

        if input_count > 1:
            command.extend(
                [
                    "-filter_complex",
                    self.build_concat_filter(
                        input_count
                    ),
                    "-map",
                    "[out]",
                ]
            )

        command.append(
            output_path
        )

        return command

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
