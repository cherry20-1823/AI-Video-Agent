from vda.agents import DirectorAgent
from vda.models.project_plan import MediaType


def test_director_agent_creates_project_plan():
    plan = DirectorAgent().create_plan(
        "做一个 60 秒关于黑洞的纪录片"
    )

    assert plan.title == "黑洞纪录片"
    assert plan.duration == 60
    assert plan.style == "Documentary"
    assert len(plan.scenes) == 4


def test_director_plan_duration_matches_scene_total():
    plan = DirectorAgent().create_plan(
        "做一个 60 秒关于黑洞的纪录片"
    )

    total_duration = sum(
        scene.duration for scene in plan.scenes
    )

    assert total_duration == plan.duration


def test_director_plan_contains_image_and_video_scenes():
    plan = DirectorAgent().create_plan(
        "做一个 60 秒关于黑洞的纪录片"
    )

    media_types = {
        scene.media_type for scene in plan.scenes
    }

    assert MediaType.IMAGE in media_types
    assert MediaType.VIDEO in media_types
