import json

BANNED = ["DDT", "ENDOSULFAN", "PARAQUAT"]

def guardrail_check(response):

    try:
        data = json.loads(response)
        text = str(data).upper()

        warnings = []

        for chem in BANNED:
            if chem in text:
                warnings.append(f"{chem} is banned in India")

        data["warnings"] = warnings

        return json.dumps(data)

    except:
        return response