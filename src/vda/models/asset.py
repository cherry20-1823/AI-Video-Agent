from dataclasses import dataclass
from pathlib import Path

from .enums import AssetType


@dataclass(slots=True)
class Asset:
    id: str
    name: str
    type: AssetType
    path: Path

    duration: float = 0.0
    size: int = 0
