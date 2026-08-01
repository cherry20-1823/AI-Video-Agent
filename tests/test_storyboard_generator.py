from unittest.mock import Mock

import pytest

from vda.builders.scene_prompt_builder import (
    ScenePromptBuilder,
)
from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)
from vda.models.task_result import TaskResult
from vda.services.storyboard_generator import (
    StoryboardGenerator,
)


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
        workspace_root=str(tmp_path),
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
        workspace_root=str(tmp_path),
    )

    with pytest.raises(
        ValueError,
        match="contains no scenes",
    ):
        generator.generate_first_scene(
            project=project,
        )
