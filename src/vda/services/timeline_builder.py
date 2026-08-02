from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.enums import AssetType
from vda.models.timeline import (
    Segment,
    Timeline,
    Track,
    TrackType,
)


class TimelineBuilder:

    def build(
        self,
        registry: AssetRegistry,
    ) -> Timeline:
        video_segments = []

        current_time = 0.0

        for asset in registry.by_type(
            AssetType.VIDEO
        ):
            video_segments.append(
                Segment(
                    asset_id=asset.id,
                    start=current_time,
                    duration=asset.duration,
                )
            )

            current_time += asset.duration

        return Timeline(
            tracks=[
                Track(
                    type=TrackType.VIDEO,
                    segments=video_segments,
                )
            ]
        )
