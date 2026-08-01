from pprint import pprint

from vda.config.settings import load_settings
from vda.openai.responses import OpenAIResponses
from vda.planners.openai_project_planner import OpenAIProjectPlanner


def main():
    settings = load_settings()

    planner = OpenAIProjectPlanner(
        responses=OpenAIResponses(
            api_key=settings.openai_api_key,
            model=settings.openai_text_model,
        )
    )

    plan = planner.plan(
        "做一个60秒关于黑洞的纪录片"
    )

    print()
    print("Project Plan")
    print("=" * 40)
    pprint(plan, sort_dicts=False)


if __name__ == "__main__":
    main()
