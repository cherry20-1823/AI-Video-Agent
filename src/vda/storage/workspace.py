from pathlib import Path

from vda.models.project import Project
from vda.models.scene import Scene


class Workspace:

    def __init__(self, root: str = "workspace"):
        self.root = Path(root)

    def create_project(self, project: Project):

        project_dir = self.root / project.id

        project_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        (project_dir / "output").mkdir(
            exist_ok=True,
        )

        for scene in project.scenes:
            self.create_scene(project, scene)

        return project_dir

    def create_scene(
        self,
        project: Project,
        scene: Scene,
    ):

        scene_dir = (
            self.root
            / project.id
            / f"scene-{scene.id:03d}"
        )

        scene_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        return scene_dir

    def save_prompt(
        self,
        project: Project,
        scene: Scene,
        prompt: str,
    ):

        scene_dir = self.create_scene(
            project,
            scene,
        )

        prompt_file = scene_dir / "prompt.txt"

        prompt_file.write_text(
            prompt,
            encoding="utf-8",
        )

        return prompt_file
