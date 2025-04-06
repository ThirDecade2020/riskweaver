import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_gpt4():
    prompt = "Hello, how are you?"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        print("Response:", response.choices[0].message.content.strip())
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    test_gpt4()

