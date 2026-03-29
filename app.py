import streamlit as st
from services.orchestrator import run_pipeline

st.set_page_config(page_title="AgriGuard AI", layout="wide")

# 🌾 Header
st.title("🌾 AgriGuard AI")
st.markdown("### Smart Agricultural Advisory with AI, Risk & Government Support")

col1, col2 = st.columns(2)

# 🔹 INPUT SECTION
with col1:
    st.subheader("📝 Farmer Input")

    text_input = st.text_area(
        "Describe your crop issue",
        placeholder="e.g. My rice leaves have brown spots after rainfall..."
    )

    audio_file = st.file_uploader(
        "🎤 Upload voice query",
        type=["mp3", "wav"]
    )

    analyze_btn = st.button("🚀 Analyze")

# 🔹 OUTPUT SECTION
if analyze_btn:
    with st.spinner("🤖 AI is analyzing your crop..."):

        result = run_pipeline({"text": text_input, "audio": audio_file})

        with col2:

            # 🌾 Diagnosis Card
            st.subheader("🌾 Diagnosis & Treatment")
            st.success(result.get("text", "No response available"))

            # 🇮🇳 Hindi
            st.subheader("🇮🇳 Hindi Explanation")
            st.info(result.get("hindi", "Translation unavailable"))

            # 🔊 Audio
            if result.get("audio"):
                st.audio(result["audio"], format="audio/mp3")

            # ⚠️ Risk Card
            st.subheader("⚠️ Risk Analysis")

            risk = result.get("risk", {})
            risk_percent = risk.get("risk_percent", 0)

            if risk_percent > 70:
                st.error(f"High Risk: {risk_percent}%")
            elif risk_percent > 40:
                st.warning(f"Medium Risk: {risk_percent}%")
            else:
                st.success(f"Low Risk: {risk_percent}%")

            st.write(f"Urgency: {risk.get('urgency', 'N/A')}")
            st.write(f"Action: {risk.get('action_priority', 'N/A')}")

            # 🏛️ Schemes
            st.subheader("🏛️ Government Schemes")

            schemes = result.get("schemes", [])

            if schemes and isinstance(schemes, list):
                for scheme in schemes:
                    st.markdown(f"""
                    ### 🏛️ {scheme.get('name', 'Unknown Scheme')}
                    - 📌 **Benefit:** {scheme.get('benefit', 'N/A')}
                    - 👤 **Eligibility:** {scheme.get('eligibility', 'N/A')}
                    """)
            else:
                st.info("No schemes available")

            # 📊 Confidence
            st.subheader("📊 Confidence Score")
            conf = result.get("confidence", 0)
            st.progress(conf / 100)
            st.write(f"{conf}% confidence")

            # 🌦️ Weather
            st.subheader("🌦️ Weather Context")
            w = result.get("weather", {})
            st.write(
                f"{w.get('temp', 'N/A')}°C | "
                f"{w.get('humidity', 'N/A')}% humidity | "
                f"{w.get('weather', 'N/A')}"
            )