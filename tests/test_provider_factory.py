import pytest

from vda.config.settings import Settings
from vda.factories import ProviderFactory
from vda.providers.image.mock.provider import MockImageProvider
from vda.providers.video.mock.provider import MockVideoProvider


def test_factory_creates_mock_video_provider():
    settings = Settings(
        video_provider="mock",
    )

    factory = ProviderFactory(settings)

    provider = factory.video_provider()

    assert isinstance(provider, MockVideoProvider)


def test_factory_creates_mock_image_provider():
    settings = Settings(
        image_provider="mock",
    )

    factory = ProviderFactory(settings)

    provider = factory.image_provider()

    assert isinstance(provider, MockImageProvider)


def test_factory_normalizes_provider_name():
    settings = Settings(
        image_provider=" Mock ",
        video_provider=" MOCK ",
    )

    factory = ProviderFactory(settings)

    assert isinstance(
        factory.image_provider(),
        MockImageProvider,
    )
    assert isinstance(
        factory.video_provider(),
        MockVideoProvider,
    )


def test_factory_rejects_unknown_video_provider():
    settings = Settings(
        video_provider="unknown",
    )

    factory = ProviderFactory(settings)

    with pytest.raises(
        ValueError,
        match="Unknown video provider: unknown",
    ):
        factory.video_provider()


def test_factory_rejects_unknown_image_provider():
    settings = Settings(
        image_provider="unknown",
    )

    factory = ProviderFactory(settings)

    with pytest.raises(
        ValueError,
        match="Unknown image provider: unknown",
    ):
        factory.image_provider()
