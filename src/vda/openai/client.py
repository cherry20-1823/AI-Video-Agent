from openai import OpenAI


def create_openai_client(
    api_key: str,
) -> OpenAI:
    cleaned_key = api_key.strip()

    if not cleaned_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. "
            "Add it to the .env file before using an OpenAI provider."
        )

    return OpenAI(
        api_key=cleaned_key,
    )
