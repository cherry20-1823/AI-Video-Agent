from vda.services.resume_planner import ResumePlanner
from vda.storage.workspace import Workspace


def test_scene_not_complete_when_files_missing(
    tmp_path,
):
    workspace = Workspace(root=str(tmp_path))
    planner = ResumePlanner(workspace)

    assert (
        planner.is_scene_complete(
            "project-001",
            1,
        )
        is False
    )


def test_scene_complete_when_files_exist(
    tmp_path,
):
    workspace = Workspace(root=str(tmp_path))

    prompt = workspace.prompt_path(
        "project-001",
        1,
    )

    image = workspace.image_path(
        "project-001",
        1,
    )

    prompt.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    prompt.write_text("prompt")
    image.write_text("image")

    planner = ResumePlanner(workspace)

    assert (
        planner.is_scene_complete(
            "project-001",
            1,
        )
        is True
    )
