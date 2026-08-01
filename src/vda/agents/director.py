from vda.models.project_plan import ProjectPlan
from vda.parsers import ProjectPlanParser
from vda.planners import MockProjectPlanner
from vda.planners.base import BaseProjectPlanner


class DirectorAgent:

    def __init__(
        self,
        planner: BaseProjectPlanner | None = None,
    ):
        self.planner = planner or MockProjectPlanner()
        self.parser = ProjectPlanParser()

    def create_plan(
        self,
        request: str,
    ) -> ProjectPlan:
        data = self.planner.plan(request)

        return self.parser.parse(data)
