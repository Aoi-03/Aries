import random
import threading
import time
from aries.llm import mistral_chat
from aries.utils import clean_ai_text

class SpontaneousResponder:
    def _init_(self, memory, tts, interval_range=(300, 600)):  # 5 to 10 mins
        self.memory = memory
        self.tts = tts
        self.interval_range = interval_range
        self.running = False

    def generate_spontaneous_message(self):
        prompt = "Start a friendly conversation based on recent memory."
        response = mistral_chat(prompt)
        return clean_ai_text(response)

    def start(self):
        self.running = True
        thread = threading.Thread(target=self._run, daemon=True)
        thread.start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            wait_time = random.randint(*self.interval_range)
            time.sleep(wait_time)
            if not self.running:
                break
            message = self.generate_spontaneous_message()
            print(f"\n[Aries spontaneously]: {message}")
            self.tts.speak(message)
