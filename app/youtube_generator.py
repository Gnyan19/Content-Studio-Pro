from .config import configure_model


def generate_youtube_script(topic, duration_minutes):
    client = configure_model()

    total_seconds = duration_minutes * 60

    prompt = f"""
You are a professional YouTube content strategist.

Generate a complete YouTube content package for:

Topic: {topic}
Duration: {duration_minutes} minutes ({total_seconds} seconds)

Provide:

1. 🎬 Catchy SEO Optimized Title
2. 📄 Description (150–200 words + hashtags)
3. 📝 Full Script with timestamps:
   - Hook (0:00–0:30)
   - 3–5 main segments with timestamps
   - Conclusion + Call to Action

Make it engaging, beginner-friendly, and optimized for retention.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text