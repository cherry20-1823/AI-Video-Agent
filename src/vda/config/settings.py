import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True)
class Settings:
    project_planner: str = "mock"
    image_provider: str = "mock"
    video_provider: str = "mock"

    openai_api_key: str = ""
    openai_text_model: str = "gpt-5.6"
    openai_image_model: str = "gpt-image-1"


def load_settings() -> Settings:
    load_dotenv()

    return Settings(
        project_planner=os.getenv(
            "PROJECT_PLANNER",
            "mock",
        ),
        image_provider=os.getenv(
            "IMAGE_PROVIDER",
            "mock",
        ),
        video_provider=os.getenv(
            "VIDEO_PROVIDER",
            "mock",
        ),
        openai_api_key=os.getenv(
            "OPENAI_API_KEY",
            "",
        ),
        openai_text_model=os.getenv(
            "OPENAI_TEXT_MODEL",
            "gpt-5.6",
        ),
        openai_image_model=os.getenv(
            "OPENAI_IMAGE_MODEL",
            "gpt-image-1",
        ),
    )
