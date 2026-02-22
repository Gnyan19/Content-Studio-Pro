from .config import configure_model


def generate_corporate_script(topic, purpose):
    client = configure_model()

    prompt = f"""
You are a corporate communications specialist.

Create a professional internal corporate script.

Topic: {topic}
Purpose: {purpose}

Structure:
- Opening statement
- Key message points
- Strategic alignment
- Closing summary

Tone: Professional, clear, leadership-focused.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text