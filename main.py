from app.youtube_generator import generate_youtube_script
from app.instagram_generator import generate_instagram_caption
from app.blog_generator import generate_blog
from app.ad_generator import generate_brand_ad
from app.corporate_generator import generate_corporate_script
from app.movie_generator import generate_movie_script
from app.linkedin_generator import generate_linkedin_post
from app.image_prompt_generator import generate_image_prompt


def main():
    while True:
        print("\n" + "=" * 60)
        print("🚀 CONTENT STUDIO PRO")
        print("=" * 60)
        print("1. YouTube Script Generator")
        print("2. Instagram Caption Generator")
        print("3. Blog Generator")
        print("4. Brand Advertisement Script")
        print("5. Corporate Internal Script")
        print("6. Movie Script Generator")
        print("7. LinkedIn Post Generator")
        print("8. AI Image Prompt Generator")
        print("0. Exit")
        print("=" * 60)

        choice = input("Select an option: ")

        try:
            if choice == "1":
                topic = input("Enter YouTube topic: ")
                duration = int(input("Duration in minutes: "))
                result = generate_youtube_script(topic, duration)

            elif choice == "2":
                topic = input("Enter Instagram topic: ")
                tone = input("Enter tone (engaging/professional/funny): ")
                result = generate_instagram_caption(topic, tone)

            elif choice == "3":
                topic = input("Enter Blog topic: ")
                words = int(input("Approx word count: "))
                result = generate_blog(topic, words)

            elif choice == "4":
                brand = input("Enter Brand name: ")
                product = input("Enter Product name: ")
                audience = input("Target audience: ")
                result = generate_brand_ad(brand, product, audience)

            elif choice == "5":
                topic = input("Enter Corporate topic: ")
                purpose = input("Enter Purpose: ")
                result = generate_corporate_script(topic, purpose)

            elif choice == "6":
                genre = input("Enter Movie genre: ")
                theme = input("Enter Theme: ")
                result = generate_movie_script(genre, theme)

            elif choice == "7":
                topic = input("Enter LinkedIn topic: ")
                audience = input("Target audience: ")
                result = generate_linkedin_post(topic, audience)

            elif choice == "8":
                subject = input("Enter image subject: ")
                style = input("Enter style (cinematic, realistic, anime, etc): ")
                platform = input("Platform (Midjourney/DALL-E/etc): ")
                result = generate_image_prompt(subject, style, platform)

            elif choice == "0":
                print("👋 Exiting Content Studio Pro...")
                break

            else:
                print("❌ Invalid option. Please try again.")
                continue

            print("\n" + "=" * 60)
            print(result)
            print("=" * 60)

        except Exception as e:
            print("\n⚠️ Error occurred:", e)


if __name__ == "__main__":
    main()