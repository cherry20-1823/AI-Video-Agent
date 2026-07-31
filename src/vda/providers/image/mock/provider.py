from pathlib import Path
from uuid import uuid4

from PIL import Image, ImageDraw

from vda.models.task_result import TaskResult
from vda.providers.image.base import BaseImageProvider


class MockImageProvider(BaseImageProvider):

    @property
    def name(self) -> str:
        return "mock-image"

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

        image = Image.new(
            mode="RGB",
            size=(1280, 720),
            color=(20, 20, 30),
        )

        draw = ImageDraw.Draw(image)

        draw.text(
            (60, 60),
            "Video Director Agent",
            fill="white",
        )

        draw.text(
            (60, 110),
            "Mock Image",
            fill="white",
        )

        preview = prompt[:500]

        draw.multiline_text(
            (60, 180),
            preview,
            fill="white",
            spacing=8,
        )

        image.save(output_file)

        return TaskResult(
            task_id=f"image-{uuid4().hex[:8]}",
            provider=self.name,
            status="completed",
            progress=100,
            local_file=str(output_file),
        )
