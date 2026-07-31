from dataclasses import dataclass, field
from typing import List

from .enums import ProjectStatus
from .scene import Scene


@dataclass(slots=True)
class Project:
    id: str

    title: str

    description: str

    duration: int

    aspect_ratio: str

    scenes: List[Scene] = field(default_factory=list)

    status: ProjectStatus = ProjectStatus.CREATED
