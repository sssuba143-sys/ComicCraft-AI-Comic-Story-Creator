import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found")
else:
    print("✅ API key found")

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Write one short funny sentence about a college student."
        )

        print("\nGemini response:")
        print(response.text)

    except Exception as e:
        print("\n❌ Gemini Error:")
        print(e)
models = client.models.list()

for model in models:
    print(model.name)