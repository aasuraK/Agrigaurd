
AgriGuard AI is a smart agricultural advisory system built with Streamlit. It helps farmers diagnose crop issues, assess risks, and get actionable recommendations using AI, weather data, and government scheme insights.

---

## 🚀 Features

- 🌿 Crop disease diagnosis using AI
- 🎤 Voice input support (speech-to-text)
- 📊 Risk assessment & confidence scoring
- 🌦️ Weather-based insights
- 📚 RAG-based agricultural knowledge system
- 🏛️ Government schemes recommendations
- 🌐 Multi-language support (via translation)

---

## 🧠 Architecture Overview

The app follows a modular pipeline:
Input → Context → AI → Risk → Guardrails → Response

### Key Modules:
- `input_service` – handles text/audio input
- `rag_service` – retrieves crop knowledge
- `ai_service / mistral_service` – AI inference
- `risk_service` – evaluates agricultural risks
- `guardrail_service` – ensures safe outputs
- `scheme_service` – fetches govt schemes
- `weather_service` – integrates weather insights
- `response_service` – formats final output
- `orchestrator` – runs the full pipeline

---

## 📁 Project Structure
agriguard_streamlit/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│ ├── crop_knowledge.csv
│ └── schemes.csv
│
├── services/
│ ├── ai_service.py
│ ├── mistral_service.py
│ ├── rag_service.py
│ ├── risk_service.py
│ ├── scheme_service.py
│ ├── weather_service.py
│ ├── orchestrator.py
│ └── ...
│
└── utils/
└── logger.py

---

## ⚙️ Installation

### 1. Clone the repo
git clone <your-repo-url>
cd agriguard_streamlit

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file and add:

MISTRAL_API_KEY=your_api_key_here
OPENWEATHER_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py
📌 Example Usage
Enter crop issue text
OR upload voice query
Click Analyze
Get:
Diagnosis
Treatment
Risk insights
Government schemes
🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
AI: Mistral API
Speech: Whisper / gTTS
Data: Pandas
APIs: Weather + Translation
📈 Future Improvements
Image-based disease detection
Mobile app version
Regional language voice assistant
Offline mode for rural areas
🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

📄 License

MIT License
