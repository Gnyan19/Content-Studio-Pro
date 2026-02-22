from .config import configure_model


def generate_movie_script(genre, theme):
    client = configure_model()

    prompt = f"""
You are a creative screenwriter.

Create a movie concept and opening script.

Genre: {genre}
Theme: {theme}

Provide:
1. Movie Title
2. Logline
3. Main Characters
4. 3-Act Structure Summary
5. Opening Scene Script (dialogue format)

Make it cinematic and engaging.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text