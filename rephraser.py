import os
from groq import Groq
from dotenv import load_dotenv
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_text(text):
    # Remove all dashes
    text = text.replace("—", ",")
    text = text.replace("–", ",")
    text = text.replace(" - ", ", ")
    
    # Fix double periods
    text = re.sub(r'\.\.+', '.', text)
    
    # Fix spaces before punctuation
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    
    # Fix multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Fix comma spacing
    text = re.sub(r',(?!\s)', ', ', text)
    
    return text.strip()

def rewrite_text(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=1.2,
        messages=[
            {
                "role": "system",
                "content": "You are a human student who rewrites text naturally and casually. You never sound like an AI."
            },
            {
                "role": "user",
                "content": f"""Rewrite this text to sound like a real person wrote it, not an AI.

Important rules:
- Use very casual everyday language
- Use contractions like don't, can't, it's, they're, won't, I'm
- Write short punchy sentences mixed with longer ones
- Add personal phrases like "I think", "honestly", "to be honest", "in my opinion", "look"
- Use words like "basically", "actually", "pretty much", "kind of", "really"
- Start some sentences with "And", "But", "So" like real people do
- Make it sound like you're talking to a friend
- NO dashes of any kind, use commas or periods instead
- NO formal words like furthermore, moreover, consequently, nevertheless
- NO bullet points or lists
- Return ONLY the rewritten text

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