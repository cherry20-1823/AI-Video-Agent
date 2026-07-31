from dataclasses import dataclass
from typing import Optional

from .asset import Asset
from .enums import SceneStatus


@dataclass(slots=True)
class Scene:
    id: int

    title: str

    narration: str

    duration: int

    prompt: str = ""

    provider: str = ""

    video: Optional[Asset] = None

    audio: Optional[Asset] = None

    subtitle: Optional[Asset] = None

    status: SceneStatus = SceneStatus.WAITING
