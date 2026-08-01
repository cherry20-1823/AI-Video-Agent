from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.project_plan import ProjectPlan
from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider
from vda.storage.workspace import Workspace


class StoryboardGenerator:
    def __init__(
        self,
        prompt_builder: ScenePromptBuilder,
        image_provider: BaseImageProvider,
        workspace: Workspace | None = None,
    ):
        self.prompt_builder = prompt_builder
        self.image_provider = image_provider
        self.workspace = workspace or Workspace()

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

        return self.image_provider.generate(
            prompt=prompt,
            output_path=str(image_file),
        )
