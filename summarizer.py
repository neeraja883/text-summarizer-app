import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def summarize_text(text, style="brief"):
    style_prompts = {
        "brief": "Summarize the following text in 2-3 sentences.",
        "detailed": "Give a detailed summary of the following text in bullet points.",
        "eli5": "Explain the following text simply, as if to a 10-year-old.",
    }

    prompt = style_prompts.get(style, style_prompts["brief"])

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
    )

    return response.choices[0].message.content