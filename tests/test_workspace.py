from vda.storage.workspace import Workspace


def test_workspace_creates_generic_scene_paths(
    tmp_path,
):
    workspace = Workspace(
        root=str(tmp_path)
    )

    prompt_path = workspace.prompt_path(
        project_id="project-001",
        scene_id=1,
    )

    image_path = workspace.image_path(
        project_id="project-001",
        scene_id=1,
    )

    assert prompt_path == (
        tmp_path
        / "project-001"
        / "scene-001"
        / "prompt.txt"
    )

    assert image_path == (
        tmp_path
        / "project-001"
        / "scene-001"
        / "image.png"
    )

    assert prompt_path.parent.exists()
