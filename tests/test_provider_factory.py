import pytest

from vda.config.settings import Settings
from vda.factories import ProviderFactory
from vda.providers.image.mock.provider import MockImageProvider
from vda.providers.image.openai.provider import OpenAIImageProvider
from vda.providers.video.mock.provider import MockVideoProvider


def test_factory_creates_mock_video_provider():
    factory = ProviderFactory(
        Settings(
            video_provider="mock",
        )
    )

    assert isinstance(
        factory.video_provider(),
        MockVideoProvider,
    )


def test_factory_creates_mock_image_provider():
    factory = ProviderFactory(
        Settings(
            image_provider="mock",
        )
    )

    assert isinstance(
        factory.image_provider(),
        MockImageProvider,
    )


def test_factory_creates_openai_image_provider():
    factory = ProviderFactory(
        Settings(
            image_provider="openai",
            openai_api_key="test-api-key",
        )
    )

    assert isinstance(
        factory.image_provider(),
        OpenAIImageProvider,
    )


def test_factory_rejects_missing_openai_key():
    factory = ProviderFactory(
        Settings(
            image_provider="openai",
            openai_api_key="",
        )
    )

    with pytest.raises(
        ValueError,
        match="OPENAI_API_KEY is missing",
    ):
        factory.image_provider()


def test_factory_rejects_unknown_video_provider():
    factory = ProviderFactory(
        Settings(
            video_provider="unknown",
        )
    )

    with pytest.raises(
        ValueError,
        match="Unknown video provider",
    ):
        factory.video_provider()


def test_factory_rejects_unknown_image_provider():
    factory = ProviderFactory(
        Settings(
            image_provider="unknown",
        )
    )

    with pytest.raises(
        ValueError,
        match="Unknown image provider",
    ):
        factory.image_provider()
