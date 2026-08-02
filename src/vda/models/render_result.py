from dataclasses import dataclass


@dataclass(slots=True)
class RenderResult:

    success: bool

    return_code: int

    output_path: str | None = None

    error: str | None = None
