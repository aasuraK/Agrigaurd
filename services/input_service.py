import whisper
import tempfile
import os

# Load model once to avoid reloading on every click
model = whisper.load_model("base")

def process_input(input_data):
    if input_data.get("audio") is not None:
        # Save the uploaded buffer to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(input_data["audio"].getvalue())
            tmp_path = tmp.name
        
        try:
            result = model.transcribe(tmp_path)
            return result["text"]
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path) # Clean up

    return input_data.get("text", "")