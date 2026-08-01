import pytest
from openai import OpenAI

from vda.openai.client import create_openai_client


def test_create_openai_client():
    client = create_openai_client(
        "test-api-key",
    )

    assert isinstance(client, OpenAI)


def test_create_openai_client_rejects_empty_key():
    with pytest.raises(
        ValueError,
        match="OPENAI_API_KEY is missing",
    ):
        create_openai_client("")
