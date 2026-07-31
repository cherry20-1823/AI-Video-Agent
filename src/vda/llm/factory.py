from vda.llm.base import BaseLLM
from vda.llm.mock.provider import MockLLM
from vda.llm.openai.provider import OpenAILLM


def create_llm(name: str) -> BaseLLM:

    name = name.lower()

    if name == "mock":
        return MockLLM()

    if name == "openai":
        return OpenAILLM()

    raise ValueError(f"Unknown LLM provider: {name}")
