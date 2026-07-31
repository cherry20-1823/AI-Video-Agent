from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider


class OpenAIImageProvider(BaseImageProvider):

    @property
    def name(self) -> str:
        return "openai-image"

    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:

        raise NotImplementedError(
            "Will implement in Lesson 025."
        )
