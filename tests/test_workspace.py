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

def test_workspace_cleanup_removes_extra_scene_directories(
    tmp_path,
):
    workspace = Workspace(
        root=str(tmp_path)
    )

    project_id = "project-001"

    for scene_id in range(1, 7):
        workspace.scene_dir(
            project_id=project_id,
            scene_id=scene_id,
        )

    removed = workspace.cleanup_project(
        project_id=project_id,
        expected_scene_count=4,
    )

    assert (
        tmp_path
        / project_id
        / "scene-001"
    ).exists()

    assert (
        tmp_path
        / project_id
        / "scene-004"
    ).exists()

    assert not (
        tmp_path
        / project_id
        / "scene-005"
    ).exists()

    assert not (
        tmp_path
        / project_id
        / "scene-006"
    ).exists()

    assert {
        path.name for path in removed
    } == {
        "scene-005",
        "scene-006",
    }


def test_workspace_cleanup_rejects_negative_scene_count(
    tmp_path,
):
    workspace = Workspace(
        root=str(tmp_path)
    )

    try:
        workspace.cleanup_project(
            project_id="project-001",
            expected_scene_count=-1,
        )
    except ValueError as error:
        assert "cannot be negative" in str(error)
    else:
        raise AssertionError(
            "Expected ValueError for negative scene count."
        )


def test_video_path(
    tmp_path,
):
    workspace = Workspace(
        root=str(tmp_path)
    )

    path = workspace.video_path(
        "project-001",
        1,
    )

    assert path.name == "video.mp4"

    assert (
        path.parent.name
        == "scene-001"
    )
