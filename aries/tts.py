# tts.py - Text-to-Speech Module using Kokoro TTS

from kokoro import TTS

class TextToSpeech:
    def _init_(self, voice="kokoro-voice"):
        self.tts = TTS(voice=voice)

    def speak(self, text):
        """
        Convert text to speech and play it.
        """
        try:
            audio = self.tts.speak(text)
            self.tts.play(audio)
        except Exception as e:
            print(f"[TTS Error] {e}")
