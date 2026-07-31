from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    image_provider: str = "mock"
    video_provider: str = "mock"

    openai_api_key: str = ""
    openai_image_model: str = "gpt-image-1"


def load_settings() -> Settings:
    return Settings(
        image_provider=os.getenv("IMAGE_PROVIDER", "mock"),
        video_provider=os.getenv("VIDEO_PROVIDER", "mock"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_image_model=os.getenv(
            "OPENAI_IMAGE_MODEL",
            "gpt-image-1",
        ),
    )
