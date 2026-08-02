from enum import Enum


class ProjectStatus(str, Enum):
    CREATED = "CREATED"
    PLANNING = "PLANNING"
    READY = "READY"
    GENERATING = "GENERATING"
    COMPOSING = "COMPOSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class SceneStatus(str, Enum):
    WAITING = "WAITING"
    PROMPT_READY = "PROMPT_READY"
    GENERATING = "GENERATING"
    DOWNLOADING = "DOWNLOADING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class TaskStatus(str, Enum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    RETRYING = "RETRYING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class AssetType(str, Enum):
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    SUBTITLE = "SUBTITLE"
    PROMPT = "PROMPT"
