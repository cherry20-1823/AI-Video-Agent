from dataclasses import dataclass


@dataclass(slots=True)
class CompositionResult:
    status: str
    duration: float
    output_path: str | None = None
