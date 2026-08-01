from vda.builders.scene_prompt_builder import ScenePromptBuilder
from vda.models.project_plan import (
    MediaType,
    ProjectPlan,
    ScenePlan,
)


def test_scene_prompt_builder_contains_project_and_scene_details():
    project = ProjectPlan(
        title="AI Future",
        topic="人工智能未来",
        duration=45,
        style="Cinematic technology documentary",
        audience="General audience",
    )

    scene = ScenePlan(
        id=1,
        title="智能时代序章",
        goal="展示人工智能重塑世界",
        duration=7,
        media_type=MediaType.VIDEO,
    )

    prompt = ScenePromptBuilder().build(
        project=project,
        scene=scene,
    )

    assert "AI Future" in prompt
    assert "智能时代序章" in prompt
    assert "展示人工智能重塑世界" in prompt
    assert "Cinematic technology documentary" in prompt
    assert "Create a cinematic video shot." in prompt


def test_scene_prompt_builder_uses_image_instruction():
    project = ProjectPlan(
        title="Black Hole",
        topic="黑洞",
        duration=60,
        style="Documentary",
        audience="General",
    )

    scene = ScenePlan(
        id=1,
        title="事件视界",
        goal="解释事件视界",
        duration=10,
        media_type=MediaType.IMAGE,
    )

    prompt = ScenePromptBuilder().build(
        project=project,
        scene=scene,
    )

    assert "Create a cinematic still image." in prompt
