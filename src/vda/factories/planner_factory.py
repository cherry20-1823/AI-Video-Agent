from vda.config.settings import Settings
from vda.planners.base import BaseProjectPlanner
from vda.planners.mock_project_planner import MockProjectPlanner


class PlannerFactory:

    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings

    def planner(self) -> BaseProjectPlanner:

        return MockProjectPlanner()
