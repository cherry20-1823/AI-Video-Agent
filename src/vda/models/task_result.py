from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskResult:

    task_id: str

    provider: str

    status: str

    progress: int = 0

    download_url: Optional[str] = None

    local_file: Optional[str] = None
