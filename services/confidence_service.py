import json

def calculate_confidence(response):

    try:
        data = json.loads(response)

        score = 0

        if data.get("diagnosis"): score += 20
        if data.get("treatment"): score += 20
        if data.get("dosage"): score += 20
        if data.get("organic"): score += 20
        if data.get("weather_advice"): score += 20

        return score

    except:
        return 50