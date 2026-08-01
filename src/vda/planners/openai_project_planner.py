import json

from vda.openai import OpenAIResponses
from vda.planners.base import BaseProjectPlanner
from vda.prompts import PROJECT_PLANNER_SYSTEM_PROMPT


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
        output = self.responses.generate(
            prompt=request,
            instructions=PROJECT_PLANNER_SYSTEM_PROMPT,
        )

        try:
            data = json.loads(output)
        except json.JSONDecodeError as error:
            raise ValueError(
                "OpenAI returned invalid project-plan JSON."
            ) from error

        if not isinstance(data, dict):
            raise ValueError(
                "OpenAI project plan must be a JSON object."
            )

        return data
