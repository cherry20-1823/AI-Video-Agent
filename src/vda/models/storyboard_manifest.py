from dataclasses import dataclass, field


@dataclass(slots=True)
class StoryboardScene:
    id: int
    title: str
    prompt: str
    image: str
    status: str = "pending"


@dataclass(slots=True)
class StoryboardManifest:
    project_id: str
    project_title: str
    scenes: list[StoryboardScene] = field(default_factory=list)
