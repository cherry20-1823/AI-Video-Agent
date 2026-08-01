import base64
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from vda.providers.image.openai.provider import OpenAIImageProvider


def test_openai_image_provider_saves_image(tmp_path):
    image_bytes = b"fake-png-content"
    encoded = base64.b64encode(
        image_bytes
    ).decode("ascii")

    client = Mock()
    client.images.generate.return_value = SimpleNamespace(
        data=[
            SimpleNamespace(
                b64_json=encoded,
            )
        ]
    )

    output_path = tmp_path / "scene-001.png"

    provider = OpenAIImageProvider(
        client=client,
        model="test-image-model",
    )

    result = provider.generate(
        prompt="A cinematic black hole.",
        output_path=str(output_path),
    )

    assert output_path.read_bytes() == image_bytes
    assert result.status == "completed"
    assert result.local_file == str(output_path)

    client.images.generate.assert_called_once_with(
        model="test-image-model",
        prompt="A cinematic black hole.",
        size="1536x1024",
    )


def test_openai_image_provider_rejects_missing_data(
    tmp_path,
):
    client = Mock()
    client.images.generate.return_value = SimpleNamespace(
        data=[]
    )

    provider = OpenAIImageProvider(
        client=client,
    )

    with pytest.raises(
        RuntimeError,
        match="no image data",
    ):
        provider.generate(
            prompt="Test",
            output_path=str(
                tmp_path / "image.png"
            ),
        )


def test_openai_image_provider_rejects_empty_image(
    tmp_path,
):
    client = Mock()
    client.images.generate.return_value = SimpleNamespace(
        data=[
            SimpleNamespace(
                b64_json=None,
            )
        ]
    )

    provider = OpenAIImageProvider(
        client=client,
    )

    with pytest.raises(
        RuntimeError,
        match="empty image",
    ):
        provider.generate(
            prompt="Test",
            output_path=str(
                tmp_path / "image.png"
            ),
        )
