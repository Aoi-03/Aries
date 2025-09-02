import os

# Paths
MEMORY_FILE = r"D:\AOI_ABHIJIT\ARIES\Aries_Memory\chat_memory.json"
AUDIO_DIR = r"D:\AOI_ABHIJIT\ARIES\temp_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

# Model settings
OLLAMA_CMD = ["ollama", "run", "mistral:7b"]
KOKORO_URL = "http://localhost:8880/v1/audio/speech"
VOICE = "af_bella"
AUDIO_FORMAT = "mp3"

# System Prompt
SYSTEM_PROMPT = (
    "SYSTEM: You are Aries — a friendly, natural, and slightly witty conversational AI. "
    "Speak like a close friend: casual, concise, curious, and empathetic. "
    "Avoid robotic closers like 'If you have any questions...'. "
    "Keep humor light and real.\n"
)

MAX_PROMPT_CHARS = 3000
