# stt.py - Speech-to-Text Module using OpenAI Whisper

import whisper
import sounddevice as sd
import numpy as np

class SpeechToText:
    def _init_(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def record_and_transcribe(self, duration=5, samplerate=16000):
        """
        Record audio and transcribe to text.
        """
        try:
            print("🎤 Recording...")
            audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
            sd.wait()
            audio = np.squeeze(audio)
            result = self.model.transcribe(audio)
            return result["text"]
        except Exception as e:
            print(f"[STT Error] {e}")
            return None
