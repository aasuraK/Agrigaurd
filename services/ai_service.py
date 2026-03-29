import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# Manually point to the .env file in the parent directory
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Force clear the old credentials error we saw earlier
if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
    del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # This print will help us debug if it's still failing
    print(f"Looked for .env at: {env_path}")
    raise ValueError("GEMINI_API_KEY is missing from your .env file!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")




def call_gemini(text, context, weather):
    prompt = f"""
    You are an AI Agricultural Expert. 
    Weather: {weather['temp']}°C, {weather['humidity']}% humidity, {weather['weather']}.
    Context: {context}
    Farmer Query: {text}

    Provide advice in this EXACT format:
    DIAGNOSIS: [Disease name]
    TREATMENT: [Main chemical or action]
    DOSAGE: [Amount per Liter]
    ORGANIC: [Bio-alternative]
    WEATHER_ADVICE: [How current weather affects this]
    """
    response = model.generate_content(prompt)
    return response.text
from services.mistral_service import call_mistral

def call_ai(text, context, weather, knowledge):

    # STEP 1: Gemini (Primary reasoning)
    gemini_output = call_gemini(text, context, weather)

    # STEP 2: Mistral (Enhancement + Structuring)
    prompt = f"""
    You are an AI Agricultural Expert.

    Weather: {weather['temp']}°C, {weather['humidity']}% humidity, {weather['weather']}.
    Context: {context}
    Farmer Query: {text}

    Respond ONLY in valid JSON. No explanation.

    Format:
    {{
    "diagnosis": "...",
    "treatment": "...",
    "dosage": "...",
    "organic": "...",
    "weather_advice": "...",
    "risk": {{
        "level": "LOW/MEDIUM/HIGH",
        "confidence": "0-100%"
    }},
    "schemes": [
        {{
        "name": "...",
        "benefit": "...",
        "eligibility": "..."
        }}
    ]
    }}
    """

    mistral_output = call_mistral(prompt)

    return mistral_output