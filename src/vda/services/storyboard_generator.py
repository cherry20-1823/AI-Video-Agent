from pathlib import Path

from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.asset import Asset
from vda.models.asset_registry import AssetRegistry
from vda.models.enums import AssetType
from vda.models.project_plan import ProjectPlan, ScenePlan
from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider
from vda.storage.workspace import Workspace


class StoryboardGenerator:
    def __init__(
        self,
        prompt_builder: ScenePromptBuilder,
        image_provider: BaseImageProvider,
        workspace: Workspace | None = None,
        registry: AssetRegistry | None = None,
    ):
        self.prompt_builder = prompt_builder
        self.image_provider = image_provider
        self.workspace = workspace or Workspace()
        self.registry = registry or AssetRegistry()

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

        image_file = self.workspace.image_path(
            project_id=project_id,
            scene_id=scene.id,
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

        result = self.image_provider.generate(
            prompt=prompt,
            output_path=str(image_file),
        )

        self.registry.add(
            Asset(
                id=f"image:scene-{scene.id:03d}",
                name=f"Scene {scene.id} Image",
                type=AssetType.IMAGE,
                path=Path(
                    f"scene-{scene.id:03d}/image.png"
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

        results = [
            self._generate_scene(
                project=project,
                scene=scene,
                project_id=project_id,
            )
            for scene in project.scenes
        ]

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
