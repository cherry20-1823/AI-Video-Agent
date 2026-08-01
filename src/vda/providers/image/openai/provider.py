import base64
from pathlib import Path
from uuid import uuid4

from openai import OpenAI

from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider


class OpenAIImageProvider(BaseImageProvider):
    def __init__(
        self,
        client: OpenAI,
        model: str = "gpt-image-1",
    ):
        self.client = client
        self.model = model

    @property
    def name(self) -> str:
        return "openai-image"

    def generate(
        self,
        prompt: str,
        output_path: str,
    ) -> TaskResult:
        output_file = Path(output_path)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        response = self.client.images.generate(
            model=self.model,
            prompt=prompt,
            size="1536x1024",
        )

        if not response.data:
            raise RuntimeError(
                "OpenAI returned no image data."
            )

        image_base64 = response.data[0].b64_json

        if not image_base64:
            raise RuntimeError(
                "OpenAI returned an empty image."
            )

        image_bytes = base64.b64decode(
            image_base64
        )

        output_file.write_bytes(
            image_bytes
        )

        return TaskResult(
            task_id=f"openai-image-{uuid4().hex[:8]}",
            provider=self.name,
            status="completed",
            progress=100,
            local_file=str(output_file),
        )
