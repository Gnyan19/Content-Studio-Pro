from .config import configure_model


def generate_linkedin_post(topic, audience):
    client = configure_model()

    prompt = f"""
You are a LinkedIn personal branding expert.

Create a high-engagement LinkedIn post.

Topic: {topic}
Target Audience: {audience}

Include:
- Strong hook
- Insightful body
- Personal or professional tone
- Clear takeaway
- Relevant hashtags

Make it thought-leadership oriented.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text