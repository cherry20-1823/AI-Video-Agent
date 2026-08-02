from dataclasses import dataclass

from vda.models.asset_registry import AssetRegistry
from vda.models.project import Project
from vda.storage.workspace import Workspace


@dataclass(slots=True)
class PipelineContext:

    project: Project

    workspace: Workspace

    asset_registry: AssetRegistry
