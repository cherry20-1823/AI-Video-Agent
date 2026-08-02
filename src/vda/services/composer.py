from vda.models.composition import (
    CompositionResult,
)
from vda.models.timeline import (
    Timeline,
)


class Composer:

    def compose(
        self,
        timeline: Timeline,
    ) -> CompositionResult:
        duration = 0.0

        for track in timeline.tracks:
            for segment in track.segments:
                duration = max(
                    duration,
                    segment.start + segment.duration,
                )

        return CompositionResult(
            status="completed",
            duration=duration,
        )
