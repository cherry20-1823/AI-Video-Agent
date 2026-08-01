from unittest.mock import Mock

import pytest

from vda.openai.responses import OpenAIResponses


def test_openai_responses_generate_returns_output_text():
    service = OpenAIResponses(
        api_key="test-api-key",
        model="test-model",
    )

    fake_response = Mock()
    fake_response.output_text = "hello"

    service.client.responses.create = Mock(
        return_value=fake_response
    )

    result = service.generate(
        prompt="test",
        instructions="reply briefly",
    )

    assert result == "hello"


def test_openai_responses_rejects_empty_output():
    service = OpenAIResponses(
        api_key="test-api-key",
        model="test-model",
    )

    fake_response = Mock()
    fake_response.output_text = "   "

    service.client.responses.create = Mock(
        return_value=fake_response
    )

    with pytest.raises(
        RuntimeError,
        match="empty response",
    ):
        service.generate("test")
