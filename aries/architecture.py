from aries.tts import TextToSpeech
from aries.stt import SpeechToText
from aries.emotion import EmotionRecognizer
from aries.spontaneous import SpontaneousResponder
from aries.memory import MemoryManager
from aries.llm import MistralChat, Phi3Chat

class AriesArchitecture:
    def _init_(self, config):
        self.config = config

        # Initialize core components
        self.memory = MemoryManager(config['memory_path'])
        self.tts = TextToSpeech(config['tts_voice'])
        self.stt = SpeechToText(config['language'])
        self.emotion = EmotionRecognizer(config['emotion_model'])

        # LLM choice: Mistral or Phi-3
        if config['llm'] == "mistral":
            self.llm = MistralChat(model_path=config['mistral_model'])
        else:
            self.llm = Phi3Chat(model_path=config['phi3_model'])

        # Spontaneous responder
        self.spontaneous = SpontaneousResponder(
            memory=self.memory,
            tts=self.tts,
            interval_range=(300, 600)  # 5 to 10 mins
        )

    def start(self):
        # Start spontaneous conversation thread
        self.spontaneous.start()
        print("[Aries] Architecture initialized and running.")

    def stop(self):
        # Stop background threads and cleanup
        self.spontaneous.stop()
        print("[Aries] Architecture stopped.")
