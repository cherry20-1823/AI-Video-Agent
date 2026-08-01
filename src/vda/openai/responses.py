from openai import OpenAI

from vda.openai.client import create_openai_client


class OpenAIResponses:

    def __init__(
        self,
        api_key: str,
        model: str,
    ):
        self.client: OpenAI = create_openai_client(
            api_key
        )
        self.model = model

    def generate(
        self,
        prompt: str,
        instructions: str = "",
    ) -> str:
        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=prompt,
        )

        output_text = response.output_text.strip()

        if not output_text:
            raise RuntimeError(
                "OpenAI returned an empty response."
            )

        return output_text
