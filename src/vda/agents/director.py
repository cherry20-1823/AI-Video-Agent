from vda.models.project_plan import ProjectPlan
from vda.parsers import ProjectPlanParser
from vda.planners import MockProjectPlanner


class DirectorAgent:

    def __init__(self):
        self.planner = MockProjectPlanner()
        self.parser = ProjectPlanParser()

    def create_plan(
        self,
        request: str,
    ) -> ProjectPlan:
        data = self.planner.plan(request)

        return self.parser.parse(data)
