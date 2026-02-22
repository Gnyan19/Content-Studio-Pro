from .config import configure_model


def generate_blog(topic, word_count=800):
    client = configure_model()

    prompt = f"""
You are a professional blog writer.

Write a well-structured blog post on:

Topic: {topic}
Approximate length: {word_count} words

Structure:
- Title
- Introduction
- Clear headings and subheadings
- Conclusion
- Key takeaways

Make it SEO-friendly and informative.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text