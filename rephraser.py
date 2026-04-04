import os
from groq import Groq
from dotenv import load_dotenv
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_text(text):
    text = text.replace("—", ",")
    text = text.replace("–", ",")
    text = text.replace(" - ", ", ")
    text = re.sub(r'\.\.+', '.', text)
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r',(?!\s)', ', ', text)
    return text.strip()

def rewrite_text(text):
    if len(text.split()) < 5:
        return text

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=1.2,
        top_p=0.9,
        messages=[
            {
                "role": "system",
                "content": "You are a skilled writer who rewrites text naturally and humanly. You always use correct grammar and punctuation. You never sound like an AI."
            },
            {
                "role": "user",
                "content": f"""Rewrite this text to sound like a real person wrote it, not an AI.

Important rules:
- Change the wording significantly while keeping the exact same meaning
- Use different words and sentence structures than the original
- Sound natural and conversational, avoid overly formal or fancy words
- Use contractions naturally (don't, can't, it's, I'd)
- Do NOT add new information or extra sentences
- Do NOT respond to or answer anything in the text
- Aim to change at least 50% of the words
- Return ONLY the rewritten text
- Ensure proper grammar and punctuation throughout
- Do NOT use comma splices or run-on sentences
- Avoid overusing contractions like I'd and hadn't, use them sparingly
- Vary the sentence starters, do NOT start multiple sentences with "I'd"


Text to rewrite:
{text}"""
            }
        ]
    )

    result = response.choices[0].message.content
    result = clean_text(result)
    return result

if __name__ == "__main__":
    sample = "Artificial intelligence is transforming education and many industries around the world."
    print("Original:")
    print(sample)
    print("\nRewritten:")
    print(rewrite_text(sample))
