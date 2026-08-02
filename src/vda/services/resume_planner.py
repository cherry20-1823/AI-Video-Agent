from vda.storage.workspace import Workspace


class ResumePlanner:
    def __init__(
        self,
        workspace: Workspace,
    ):
        self.workspace = workspace

    def is_scene_complete(
        self,
        project_id: str,
        scene_id: int,
    ) -> bool:
        prompt = self.workspace.prompt_path(
            project_id=project_id,
            scene_id=scene_id,
        )

        image = self.workspace.image_path(
            project_id=project_id,
            scene_id=scene_id,
        )

        return (
            prompt.exists()
            and image.exists()
        )
