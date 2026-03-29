from services.mistral_service import call_mistral

def assess_risk(text, weather):

    prompt = f"""
    कृषि जोखिम विश्लेषण:

    Problem: {text}
    Weather: {weather}

    Return JSON:
    {{
        "risk_percent": int,
        "urgency": "LOW/MEDIUM/HIGH",
        "action_priority": "IMMEDIATE/NORMAL/MONITOR"
    }}
    """

    try:
        return eval(call_mistral(prompt))
    except:
        return {
            "risk_percent": 50,
            "urgency": "MEDIUM",
            "action_priority": "NORMAL"
        }