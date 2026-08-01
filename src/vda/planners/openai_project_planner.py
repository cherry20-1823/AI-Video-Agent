from vda.openai import OpenAIResponses
from vda.planners.base import BaseProjectPlanner


class OpenAIProjectPlanner(BaseProjectPlanner):

    def __init__(self):
        self.responses = OpenAIResponses()

    def plan(
        self,
        request: str,
    ) -> dict:

        raise NotImplementedError(
            "Will implement in Milestone 4.3"
        )
