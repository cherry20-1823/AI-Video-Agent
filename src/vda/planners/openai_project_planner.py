from vda.planners.base import BaseProjectPlanner


class OpenAIProjectPlanner(BaseProjectPlanner):

    def plan(
        self,
        request: str,
    ) -> dict:

        raise NotImplementedError(
            "Will implement in Milestone 4.3"
        )
