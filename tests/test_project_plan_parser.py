from vda.models.project_plan import MediaType
from vda.parsers import ProjectPlanParser


def test_project_plan_parser():

    parser = ProjectPlanParser()

    data = {
        "title": "黑洞纪录片",
        "topic": "黑洞",
        "duration": 60,
        "style": "Documentary",
        "audience": "General",
        "scenes": [
            {
                "title": "什么是黑洞",
                "goal": "解释黑洞",
                "duration": 15,
                "media_type": "image",
            },
            {
                "title": "事件视界",
                "goal": "解释事件视界",
                "duration": 45,
                "media_type": "video",
            },
        ],
    }

    plan = parser.parse(data)

    assert plan.title == "黑洞纪录片"

    assert len(plan.scenes) == 2

    assert (
        plan.scenes[0].media_type
        == MediaType.IMAGE
    )

    assert (
        plan.scenes[1].media_type
        == MediaType.VIDEO
    )
