import json
from pathlib import Path

from vda.models.project import Project
from vda.models.scene import Scene


class Workspace:

    def __init__(self, root: str = "workspace"):
        self.root = Path(root)

    def project_dir(
        self,
        project_id: str,
    ) -> Path:
        path = self.root / project_id
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    def scene_dir(
        self,
        project_id: str,
        scene_id: int,
    ) -> Path:
        path = (
            self.project_dir(project_id)
            / f"scene-{scene_id:03d}"
        )
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    def prompt_path(
        self,
        project_id: str,
        scene_id: int,
    ) -> Path:
        return (
            self.scene_dir(
                project_id,
                scene_id,
            )
            / "prompt.txt"
        )

    def image_path(
        self,
        project_id: str,
        scene_id: int,
    ) -> Path:
        return (
            self.scene_dir(
                project_id,
                scene_id,
            )
            / "image.png"
        )


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


    def save_manifest(
        self,
        project_dir: Path,
        manifest: dict,
    ):

        manifest_file = (
            project_dir
            / "storyboard.json"
        )

        manifest_file.write_text(
            json.dumps(
                manifest,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return manifest_file


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
