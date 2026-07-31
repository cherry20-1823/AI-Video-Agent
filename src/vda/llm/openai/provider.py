from vda.llm.base import BaseLLM


class OpenAILLM(BaseLLM):

    def generate_plan(self, topic: str) -> dict:
        raise NotImplementedError(
            "OpenAI provider has not been implemented yet."
        )
