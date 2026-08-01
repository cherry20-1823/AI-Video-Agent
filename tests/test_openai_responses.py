from vda.openai.responses import OpenAIResponses


def test_openai_responses_has_generate():
    assert hasattr(
        OpenAIResponses,
        "generate",
    )
