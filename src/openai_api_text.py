from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-nano",
    input="Describe an AI learning about humans for the first time, using only two silly sentences."
)

print(response.output_text)