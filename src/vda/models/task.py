from dataclasses import dataclass

from .enums import TaskStatus


@dataclass(slots=True)
class Task:
    id: str

    scene_id: int

    provider: str

    remote_task_id: str = ""

    status: TaskStatus = TaskStatus.QUEUED
