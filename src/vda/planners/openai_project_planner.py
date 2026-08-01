from vda.openai import OpenAIResponses
from vda.planners.base import BaseProjectPlanner


class OpenAIProjectPlanner(BaseProjectPlanner):

    def __init__(
        self,
        responses: OpenAIResponses,
    ):
        self.responses = responses

    def plan(
        self,
        request: str,
    ) -> dict:

        raise NotImplementedError(
            "Will implement in Milestone 4.3"
        )
