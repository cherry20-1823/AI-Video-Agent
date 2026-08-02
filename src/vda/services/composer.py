from vda.models.composition import (
    CompositionResult,
)
from vda.models.timeline import (
    Timeline,
)
from vda.renderers.base import (
    BaseRenderer,
)


class Composer:

    def __init__(
        self,
        renderer: BaseRenderer | None = None,
    ):
        self.renderer = renderer

    def compose(
        self,
        timeline: Timeline,
        output_path: str | None = None,
    ) -> CompositionResult:
        duration = 0.0

        for track in timeline.tracks:
            for segment in track.segments:
                duration = max(
                    duration,
                    segment.start + segment.duration,
                )

        rendered_path = output_path

        if (
            self.renderer is not None
            and output_path is not None
        ):
            rendered_path = self.renderer.render(
                timeline,
                output_path,
            )

        return CompositionResult(
            status="completed",
            duration=duration,
            output_path=rendered_path,
        )
