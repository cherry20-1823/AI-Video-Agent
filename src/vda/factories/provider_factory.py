from vda.config.settings import Settings
from vda.openai.client import create_openai_client
from vda.providers.image.base import BaseImageProvider
from vda.providers.image.mock.provider import MockImageProvider
from vda.providers.image.openai.provider import OpenAIImageProvider
from vda.providers.video.base import BaseVideoProvider
from vda.providers.video.mock.provider import MockVideoProvider


class ProviderFactory:
    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings

    def video_provider(
        self,
    ) -> BaseVideoProvider:
        provider_name = (
            self.settings.video_provider
            .strip()
            .lower()
        )

        if provider_name == "mock":
            return MockVideoProvider()

        raise ValueError(
            f"Unknown video provider: {provider_name}"
        )

    def image_provider(
        self,
    ) -> BaseImageProvider:
        provider_name = (
            self.settings.image_provider
            .strip()
            .lower()
        )

        if provider_name == "mock":
            return MockImageProvider()

        if provider_name == "openai":
            client = create_openai_client(
                self.settings.openai_api_key
            )

            return OpenAIImageProvider(
                client=client,
                model=self.settings.openai_image_model,
            )

        raise ValueError(
            f"Unknown image provider: {provider_name}"
        )
