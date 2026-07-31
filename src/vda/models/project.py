from dataclasses import dataclass, field
from typing import List

from .scene import Scene
from .enums import ProjectStatus


@dataclass(slots=True)
class Project:
    id: str

    title: str

    description: str

    duration: int

    aspect_ratio: str

    scenes: List[Scene] = field(default_factory=list)

    status: ProjectStatus = ProjectStatus.CREATED
