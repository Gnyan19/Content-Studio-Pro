from .config import configure_model


def generate_brand_ad(brand_name, product, target_audience):
    client = configure_model()

    prompt = f"""
You are a professional advertising copywriter.

Create a high-converting advertisement script for:

Brand: {brand_name}
Product: {product}
Target Audience: {target_audience}

Include:
1. Attention-grabbing hook
2. Problem statement
3. Product benefits
4. Emotional appeal
5. Strong call to action

Make it persuasive, clear, and impactful.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text