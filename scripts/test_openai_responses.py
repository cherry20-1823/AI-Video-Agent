from vda.config.settings import load_settings
from vda.openai.responses import OpenAIResponses


def main():
    settings = load_settings()

    service = OpenAIResponses(
        api_key=settings.openai_api_key,
        model=settings.openai_text_model,
    )

    result = service.generate(
        prompt="Reply with exactly: Hello VDA",
        instructions="Return plain text only.",
    )

    print()
    print("Response")
    print("--------")
    print(result)


if __name__ == "__main__":
    main()
