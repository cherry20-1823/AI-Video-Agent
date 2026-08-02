from pathlib import Path

from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.asset import Asset
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType
from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)
from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider
from vda.providers.video.base import BaseVideoProvider
from vda.services.resume_planner import ResumePlanner
from vda.storage.workspace import Workspace


class StoryboardGenerator:
    def __init__(
        self,
        prompt_builder: ScenePromptBuilder,
        image_provider: BaseImageProvider,
        video_provider: BaseVideoProvider | None = None,
        workspace: Workspace | None = None,
        registry: AssetRegistry | None = None,
        resume_planner: ResumePlanner | None = None,
    ):
        self.prompt_builder = prompt_builder
        self.image_provider = image_provider
        self.video_provider = video_provider
        self.workspace = workspace or Workspace()
        self.registry = registry or AssetRegistry()
        self.resume_planner = (
            resume_planner
            or ResumePlanner(self.workspace)
        )

    def _get_provider(
        self,
        scene: ScenePlan,
    ):
        if (
            scene.media_type == MediaType.VIDEO
            and self.video_provider is not None
        ):
            return self.video_provider

        return self.image_provider

    def _get_output_path(
        self,
        project_id: str,
        scene: ScenePlan,
    ):
        if scene.media_type == MediaType.VIDEO:
            return self.workspace.video_path(
                project_id=project_id,
                scene_id=scene.id,
            )

        return self.workspace.image_path(
            project_id=project_id,
            scene_id=scene.id,
        )

    def _get_asset_type(
        self,
        scene: ScenePlan,
    ) -> AssetType:
        if scene.media_type == MediaType.VIDEO:
            return AssetType.VIDEO

        return AssetType.IMAGE

    def _get_asset_path(
        self,
        scene: ScenePlan,
    ) -> Path:
        if scene.media_type == MediaType.VIDEO:
            return Path(
                f"scene-{scene.id:03d}/video.mp4"
            )

        return Path(
            f"scene-{scene.id:03d}/image.png"
        )

    def _generate_scene(
        self,
        project: ProjectPlan,
        scene: ScenePlan,
        project_id: str,
    ) -> TaskResult:
        prompt = self.prompt_builder.build(
            project=project,
            scene=scene,
        )

        prompt_file = self.workspace.prompt_path(
            project_id=project_id,
            scene_id=scene.id,
        )

        output_file = self._get_output_path(
            project_id=project_id,
            scene=scene,
        )

        prompt_file.write_text(
            prompt,
            encoding="utf-8",
        )

        self.registry.add(
            Asset(
                id=f"prompt:scene-{scene.id:03d}",
                name=f"Scene {scene.id} Prompt",
                type=AssetType.PROMPT,
                path=Path(
                    f"scene-{scene.id:03d}/prompt.txt"
                ),
            )
        )

        provider = self._get_provider(
            scene
        )

        result = provider.generate(
            prompt=prompt,
            output_path=str(output_file),
        )

        asset_type = self._get_asset_type(
            scene
        )

        self.registry.add(
            Asset(
                id=(
                    f"{asset_type.value.lower()}"
                    f":scene-{scene.id:03d}"
                ),
                name=f"Scene {scene.id} Asset",
                type=asset_type,
                path=self._get_asset_path(
                    scene
                ),
            )
        )

        return result

    def generate_all(
        self,
        project: ProjectPlan,
        project_id: str = "project-001",
    ) -> list[TaskResult]:
        if not project.scenes:
            raise ValueError(
                "Project plan contains no scenes."
            )

        self.workspace.cleanup_project(
            project_id=project_id,
            expected_scene_count=len(project.scenes),
        )

        results = []

        for scene in project.scenes:
            if self.resume_planner.is_scene_complete(
                project_id=project_id,
                scene_id=scene.id,
            ):
                continue

            results.append(
                self._generate_scene(
                    project=project,
                    scene=scene,
                    project_id=project_id,
                )
            )

        manifest = {
            "project_id": project_id,
            "project_title": project.title,
            "total_scenes": len(project.scenes),
            "scenes": [
                {
                    "id": scene.id,
                    "title": scene.title,
                    "prompt": (
                        f"scene-{scene.id:03d}/prompt.txt"
                    ),
                    "image": (
                        f"scene-{scene.id:03d}/image.png"
                    ),
                    "status": "completed",
                }
                for scene in project.scenes
            ],
        }

        project_dir = self.workspace.project_dir(
            project_id
        )

        self.workspace.save_manifest(
            project_dir=project_dir,
            manifest=manifest,
        )

        return results

    def generate_first_scene(
        self,
        project: ProjectPlan,
        project_id: str = "project-001",
    ) -> TaskResult:
        if not project.scenes:
            raise ValueError(
                "Project plan contains no scenes."
            )

        return self._generate_scene(
            project=project,
            scene=project.scenes[0],
            project_id=project_id,
        )
