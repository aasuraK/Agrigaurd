import io
import json
import re
from deep_translator import GoogleTranslator
from gtts import gTTS


def extract_json(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        return None
    return None


def safe_get(value, key=None, default="N/A"):
    if isinstance(value, dict):
        return value.get(key, default)
    return value if value else default


def format_response(raw_text):

    data = extract_json(raw_text)

    if data:
        # 🧠 Robust parsing (handles string + dict)
        diagnosis = safe_get(data.get("diagnosis"), "name")

        treatment_data = data.get("treatment")
        if isinstance(treatment_data, dict):
            treatment = safe_get(treatment_data.get("chemical"), "name")
        else:
            treatment = treatment_data or "N/A"

        dosage = safe_get(data.get("dosage"), "unit", "Follow instructions")

        organic_data = data.get("organic")
        if isinstance(organic_data, dict):
            organic_list = organic_data.get("alternatives", [])
            organic = ", ".join(organic_list) if organic_list else "Not available"
        else:
            organic = organic_data or "Not available"

        weather = safe_get(data.get("weather_advice"), "risk_assessment", "No weather data")

        formatted = f"""
🌾 Diagnosis: {diagnosis}

🧪 Treatment: {treatment}

💧 Dosage: {dosage}

🌿 Organic Option: {organic}

🌦️ Weather Advice:
- {weather}
""".strip()

    else:
        formatted = re.sub(r"\{.*\}", "", raw_text, flags=re.DOTALL).strip()

    # 🌐 Translation
    try:
        hindi_translation = GoogleTranslator(source='auto', target='hi').translate(formatted)
    except:
        hindi_translation = "अनुवाद त्रुटि"

    # 🔊 Audio
    try:
        tts = gTTS(hindi_translation, lang='hi')
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_data = audio_fp.getvalue()
    except:
        audio_data = None

    return {
        "text": formatted,
        "hindi": hindi_translation,
        "audio": audio_data
    }