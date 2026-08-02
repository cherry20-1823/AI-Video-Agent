from dataclasses import dataclass

from vda.models.asset_registry import AssetRegistry
from vda.models.project import Project
from vda.models.timeline import Timeline
from vda.providers.video.base import BaseVideoProvider
from vda.storage.workspace import Workspace


@dataclass(slots=True)
class PipelineContext:

    topic: str

    workspace: Workspace

    asset_registry: AssetRegistry

    project: Project | None = None

    timeline: Timeline | None = None

    video_provider: BaseVideoProvider | None = None
