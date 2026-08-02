from pathlib import Path

from vda.models.asset import Asset
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType
from vda.providers.video.base import BaseVideoProvider
from vda.storage.workspace import Workspace


class VideoGenerator:
    def __init__(
        self,
        video_provider: BaseVideoProvider,
        workspace: Workspace,
        registry: AssetRegistry | None = None,
    ):
        self.video_provider = video_provider
        self.workspace = workspace
        self.registry = registry or AssetRegistry()

    def generate(
        self,
        project_id: str,
        scene_id: int,
        prompt: str,
    ):
        video_path = self.workspace.video_path(
            project_id,
            scene_id,
        )

        result = self.video_provider.generate(
            prompt=prompt,
            output_path=str(video_path),
        )

        self.registry.add(
            Asset(
                id=f"video:scene-{scene_id:03d}",
                name=f"Scene {scene_id} Video",
                type=AssetType.VIDEO,
                path=Path(
                    f"scene-{scene_id:03d}/video.mp4"
                ),
            )
        )

        return result
