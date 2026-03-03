from openai import OpenAI
from app.core.config import get_settings

settings = get_settings()

client = OpenAI(api_key=settings.openai_api_key)

def test_openai() -> str:
    if settings.environment == "development":
        return "Mocked OpenAI response (dev mode)"

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Say hello in one short sentence."
    )
    return response.output_text