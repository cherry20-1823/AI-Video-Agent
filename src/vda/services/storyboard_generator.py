from pathlib import Path

from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.project_plan import ProjectPlan
from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider


class StoryboardGenerator:
    def __init__(
        self,
        prompt_builder: ScenePromptBuilder,
        image_provider: BaseImageProvider,
        workspace_root: str = "workspace",
    ):
        self.prompt_builder = prompt_builder
        self.image_provider = image_provider
        self.workspace_root = Path(workspace_root)

    def generate_first_scene(
        self,
        project: ProjectPlan,
        project_id: str = "project-001",
    ) -> TaskResult:
        if not project.scenes:
            raise ValueError(
                "Project plan contains no scenes."
            )

        scene = project.scenes[0]

        prompt = self.prompt_builder.build(
            project=project,
            scene=scene,
        )

        scene_dir = (
            self.workspace_root
            / project_id
            / f"scene-{scene.id:03d}"
        )

        scene_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        prompt_file = scene_dir / "prompt.txt"
        image_file = scene_dir / "image.png"

        prompt_file.write_text(
            prompt,
            encoding="utf-8",
        )

        return self.image_provider.generate(
            prompt=prompt,
            output_path=str(image_file),
        )
