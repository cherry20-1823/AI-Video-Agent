from unittest.mock import Mock

import pytest

from vda.planners.openai_project_planner import OpenAIProjectPlanner


def test_openai_project_planner_parses_json():
    responses = Mock()
    responses.generate.return_value = """
    {
        "title": "黑洞纪录片",
        "topic": "黑洞",
        "duration": 60,
        "style": "Documentary",
        "audience": "General",
        "scenes": []
    }
    """

    planner = OpenAIProjectPlanner(
        responses=responses,
    )

    result = planner.plan(
        "做一个60秒关于黑洞的纪录片"
    )

    assert result["title"] == "黑洞纪录片"
    assert result["duration"] == 60


def test_openai_project_planner_rejects_invalid_json():
    responses = Mock()
    responses.generate.return_value = "not valid json"

    planner = OpenAIProjectPlanner(
        responses=responses,
    )

    with pytest.raises(
        ValueError,
        match="invalid project-plan JSON",
    ):
        planner.plan("制作一个纪录片")
