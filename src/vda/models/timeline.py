from dataclasses import dataclass, field
from enum import Enum


class TrackType(str, Enum):
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    SUBTITLE = "SUBTITLE"


@dataclass(slots=True)
class Segment:
    asset_id: str
    start: float
    duration: float


@dataclass(slots=True)
class Track:
    type: TrackType
    segments: list[Segment] = field(
        default_factory=list
    )


@dataclass(slots=True)
class Timeline:
    tracks: list[Track] = field(
        default_factory=list
    )
