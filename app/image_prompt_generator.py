from .config import configure_model


def generate_image_prompt(subject, style, platform):
    client = configure_model()

    prompt = f"""
You are a professional AI image prompt engineer.

Create a highly detailed AI image generation prompt.

Subject: {subject}
Style: {style}
Platform: {platform}

Requirements:
- Very detailed description
- Camera angle
- Lighting
- Mood
- Color grading
- Environment details
- High-resolution quality keywords
- Cinematic / artistic enhancements

Make it optimized for platforms like Midjourney, DALL-E, Leonardo AI, etc.
Return only the final image prompt text.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text