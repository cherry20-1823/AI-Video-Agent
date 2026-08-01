from vda.config.settings import Settings
from vda.planners.base import BaseProjectPlanner
from vda.planners.mock_project_planner import MockProjectPlanner
from vda.planners.openai_project_planner import OpenAIProjectPlanner


class PlannerFactory:

    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings

    def planner(self) -> BaseProjectPlanner:

        planner = getattr(
            self.settings,
            "project_planner",
            "mock",
        ).strip().lower()

        if planner == "mock":
            return MockProjectPlanner()

        if planner == "openai":
            return OpenAIProjectPlanner()

        raise ValueError(
            f"Unknown project planner: {planner}"
        )
