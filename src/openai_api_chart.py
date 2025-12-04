from openai import OpenAI
import os
from dotenv import load_dotenv
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

chart_path = "./data/optuna_chart.png"

# OpenAI requires base64 encoding for local images
with open(chart_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

chart_response = client.chat.completions.create(
    model="gpt-4o",  # Using vision-capable model
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Please analyze this Optuna hyperparameter optimization chart and provide a detailed explanation. Include: 1) What type of chart/visualization this is, 2) What hyperparameters are being shown, 3) What the trends and patterns indicate, 4) Any insights about the optimization process, and 5) Recommendations based on the results."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=1000
)

print("\n" + "="*80)
print("OPTUNA CHART ANALYSIS")
print("="*80)
print(chart_response.choices[0].message.content)