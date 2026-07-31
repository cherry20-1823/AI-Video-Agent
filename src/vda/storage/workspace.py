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
