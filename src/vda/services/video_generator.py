
from vda.models.asset import Asset
from vda.models.context import (
    PipelineContext,
)
from vda.models.enums import AssetType
from vda.providers.video.base import BaseVideoProvider


class VideoGenerator:
    def __init__(
        self,
        video_provider: BaseVideoProvider,
        context: PipelineContext,
    ):
        self.video_provider = video_provider
        self.context = context

    def generate(
        self,
        project_id: str,
        scene_id: int,
        prompt: str,
    ):
        video_path = self.context.workspace.video_path(
            project_id,
            scene_id,
        )

        result = self.video_provider.generate(
            prompt=prompt,
            output_path=str(video_path),
        )

        downloaded_path = (
            self.video_provider.download(
                result
            )
        )

        self.context.asset_registry.add(
            Asset(
                id=f"video:scene-{scene_id:03d}",
                name=f"Scene {scene_id} Video",
                type=AssetType.VIDEO,
                path=downloaded_path,
            )
        )

        return result
