from dataclasses import dataclass, field
from enum import Enum


class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


@dataclass(slots=True)
class ScenePlan:
    id: int
    title: str
    goal: str
    duration: int
    media_type: MediaType


@dataclass(slots=True)
class ProjectPlan:
    title: str
    topic: str
    duration: int
    style: str
    audience: str
    scenes: list[ScenePlan] = field(default_factory=list)
