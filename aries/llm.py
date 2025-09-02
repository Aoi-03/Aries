import subprocess
from aries.config import OLLAMA_CMD

def mistral_chat(prompt):
    try:
        result = subprocess.run(
            OLLAMA_CMD,
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Ollama error:", result.stderr[:500])
            return "Sorry, I had trouble responding."
    except Exception as e:
        print("Failed to run ollama:", e)
        return "Sorry, I had trouble responding."
