import json
from pathlib import Path
from unittest.mock import Mock

import pytest

from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.asset_registry import (
    AssetRegistry,
)
from vda.models.enums import AssetType
from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)
from vda.models.task_result import TaskResult
from vda.services.storyboard_generator import (
    StoryboardGenerator,
)
from vda.storage.workspace import Workspace


def create_project() -> ProjectPlan:
    project = ProjectPlan(
        title="AI Future",
        topic="人工智能未来",
        duration=45,
        style="Technology documentary",
        audience="General audience",
    )

    project.scenes.append(
        ScenePlan(
            id=1,
            title="智能时代序章",
            goal="展示人工智能重塑世界",
            duration=7,
            media_type=MediaType.IMAGE,
        )
    )

    return project


def test_storyboard_generator_creates_first_scene(
    tmp_path,
):
    image_provider = Mock()
    image_provider.generate.return_value = TaskResult(
        task_id="image-001",
        provider="mock",
        status="completed",
        progress=100,
        local_file=str(
            tmp_path / "image.png"
        ),
    )

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        workspace=Workspace(
            root=str(tmp_path)
        ),
    )

    result = generator.generate_first_scene(
        project=create_project(),
        project_id="test-project",
    )

    prompt_file = (
        tmp_path
        / "test-project"
        / "scene-001"
        / "prompt.txt"
    )

    assert prompt_file.exists()
    assert "智能时代序章" in (
        prompt_file.read_text(
            encoding="utf-8"
        )
    )
    assert result.status == "completed"

    image_provider.generate.assert_called_once()


def test_storyboard_generator_rejects_empty_project(
    tmp_path,
):
    project = ProjectPlan(
        title="Empty",
        topic="Empty",
        duration=0,
        style="None",
        audience="None",
    )

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=Mock(),
        workspace=Workspace(
            root=str(tmp_path)
        ),
    )

    with pytest.raises(
        ValueError,
        match="contains no scenes",
    ):
        generator.generate_first_scene(
            project=project,
        )

def test_storyboard_generator_writes_manifest(
    tmp_path,
):
    project = create_project()

    second_scene = ScenePlan(
        id=2,
        title="产业革新",
        goal="展示人工智能改变产业",
        duration=8,
        media_type=MediaType.IMAGE,
    )
    project.scenes.append(second_scene)

    image_provider = Mock()
    image_provider.generate.side_effect = [
        TaskResult(
            task_id="image-001",
            provider="mock",
            status="completed",
            progress=100,
            local_file=str(
                tmp_path
                / "test-project"
                / "scene-001"
                / "image.png"
            ),
        ),
        TaskResult(
            task_id="image-002",
            provider="mock",
            status="completed",
            progress=100,
            local_file=str(
                tmp_path
                / "test-project"
                / "scene-002"
                / "image.png"
            ),
        ),
    ]

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        workspace=Workspace(
            root=str(tmp_path)
        ),
    )

    results = generator.generate_all(
        project=project,
        project_id="test-project",
    )

    manifest_path = (
        tmp_path
        / "test-project"
        / "storyboard.json"
    )

    assert manifest_path.exists()
    assert len(results) == 2

    manifest = json.loads(
        manifest_path.read_text(
            encoding="utf-8"
        )
    )

    assert manifest["project_id"] == "test-project"
    assert manifest["project_title"] == "AI Future"
    assert manifest["total_scenes"] == 2

    assert manifest["scenes"][0] == {
        "id": 1,
        "title": "智能时代序章",
        "prompt": "scene-001/prompt.txt",
        "image": "scene-001/image.png",
        "status": "completed",
    }

    assert manifest["scenes"][1]["id"] == 2
    assert manifest["scenes"][1]["status"] == "completed"

    assert image_provider.generate.call_count == 2



def test_storyboard_generator_registers_prompt_assets(
    tmp_path,
):
    project = create_project()

    image_provider = Mock()
    image_provider.generate.return_value = TaskResult(
        task_id="image-001",
        provider="mock",
        status="completed",
        progress=100,
        local_file=str(
            tmp_path
            / "project-001"
            / "scene-001"
            / "image.png"
        ),
    )

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        workspace=Workspace(
            root=str(tmp_path)
        ),
    )

    generator.generate_all(
        project=project,
        project_id="project-001",
    )

    prompt_assets = generator.registry.by_type(
        AssetType.PROMPT
    )

    assert len(prompt_assets) == 1
    assert prompt_assets[0].id == "prompt:scene-001"
    assert prompt_assets[0].path == Path(
        "scene-001/prompt.txt"
    )


def test_storyboard_generator_skips_completed_scene(
    tmp_path,
):
    project = create_project()

    workspace = Workspace(
        root=str(tmp_path)
    )

    prompt_file = workspace.prompt_path(
        project_id="project-001",
        scene_id=1,
    )
    image_file = workspace.image_path(
        project_id="project-001",
        scene_id=1,
    )

    prompt_file.write_text(
        "existing prompt",
        encoding="utf-8",
    )
    image_file.write_text(
        "existing image",
        encoding="utf-8",
    )

    image_provider = Mock()

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        workspace=workspace,
    )

    results = generator.generate_all(
        project=project,
        project_id="project-001",
    )

    assert results == []
    image_provider.generate.assert_not_called()


def test_storyboard_generator_generates_video_scene(
    tmp_path,
):
    project = ProjectPlan(
        title="AI Future",
        topic="AI Video",
        duration=10,
        style="cinematic",
        audience="General",
    )

    project.scenes.append(
        ScenePlan(
            id=1,
            title="AI Motion",
            goal="Generate AI video",
            duration=5,
            media_type=MediaType.VIDEO,
        )
    )

    image_provider = Mock()

    video_provider = Mock()
    video_provider.generate.return_value = TaskResult(
        task_id="video-001",
        provider="mock-video",
        status="completed",
        progress=100,
        local_file=str(
            tmp_path / "video.mp4"
        ),
    )

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        video_provider=video_provider,
        workspace=Workspace(
            root=str(tmp_path)
        ),
    )

    result = generator.generate_first_scene(
        project=project,
        project_id="video-project",
    )

    assert result.status == "completed"

    video_provider.generate.assert_called_once()

    image_provider.generate.assert_not_called()


def test_storyboard_generator_registers_video_asset(
    tmp_path,
):
    project = ProjectPlan(
        title="AI Future",
        topic="AI Video",
        duration=10,
        style="cinematic",
        audience="General",
    )

    project.scenes.append(
        ScenePlan(
            id=1,
            title="AI Motion",
            goal="Generate AI video",
            duration=5,
            media_type=MediaType.VIDEO,
        )
    )

    image_provider = Mock()

    video_provider = Mock()
    video_provider.generate.return_value = TaskResult(
        task_id="video-001",
        provider="mock-video",
        status="completed",
        progress=100,
        local_file=str(
            tmp_path / "video.mp4"
        ),
    )

    registry = AssetRegistry()

    generator = StoryboardGenerator(
        prompt_builder=ScenePromptBuilder(),
        image_provider=image_provider,
        video_provider=video_provider,
        workspace=Workspace(
            root=str(tmp_path)
        ),
        registry=registry,
    )

    generator.generate_first_scene(
        project=project,
        project_id="video-project",
    )

    videos = registry.by_type(
        AssetType.VIDEO
    )

    assert len(videos) == 1

    assert videos[0].id == (
        "video:scene-001"
    )

    assert videos[0].path == Path(
        "scene-001/video.mp4"
    )
