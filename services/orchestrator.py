from services.input_service import process_input
from services.context_service import get_context
from services.rag_service import retrieve_knowledge
from services.ai_service import call_ai
from services.guardrail_service import guardrail_check
from services.response_service import format_response
from services.weather_service import get_weather
from services.confidence_service import calculate_confidence
from services.scheme_service import get_schemes
from services.risk_service import assess_risk
from utils.logger import log

def run_pipeline(input_data):

    log("Processing input")

    text = process_input(input_data)

    weather = get_weather()

    context = get_context(text)

    knowledge = retrieve_knowledge(text)

    log("Calling AI models")

    ai_output = call_ai(text, context, weather, knowledge)

    safe_output = guardrail_check(ai_output)

    confidence = calculate_confidence(safe_output)

    risk = assess_risk(text, weather)
    schemes = get_schemes(text, risk, weather)
    final = format_response(safe_output)

    final["confidence"] = confidence
    final["weather"] = weather
    final["risk"] = risk
    final["schemes"] = schemes
    return final