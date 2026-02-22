from .config import configure_model


def generate_instagram_caption(topic, tone="engaging"):
    client = configure_model()

    prompt = f"""
You are a social media strategist.

Create an Instagram caption for the topic: {topic}

Tone: {tone}

Include:
- Hook line
- Short engaging body
- Call to action
- 10 relevant hashtags
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text