from vda.models.context import PipelineContext
from vda.services.planner import Planner
from vda.storage.workspace import Workspace


class PlanningStep:

    def __init__(
        self,
        planner: Planner,
        workspace: Workspace,
    ):
        self.planner = planner
        self.workspace = workspace

    def execute(
        self,
        context: PipelineContext,
    ) -> PipelineContext:

        project = self.planner.create_project(
            context.topic
        )

        context.project = project

        self.workspace.create_project(
            project
        )

        return context
