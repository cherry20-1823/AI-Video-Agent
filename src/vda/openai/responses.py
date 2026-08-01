from openai import OpenAI

from vda.openai.client import create_openai_client


class OpenAIResponses:

    def __init__(self):
        self.client: OpenAI = create_openai_client()

    def generate(
        self,
        prompt: str,
    ) -> str:
        raise NotImplementedError(
            "Will implement in Milestone 4.3.3"
        )
