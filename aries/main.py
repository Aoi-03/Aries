from aries.memory import load_memory, save_memory
from aries.utils import build_prompt_with_memory, clean_ai_text
from aries.llm import mistral_chat
from aries.tts import TextToSpeech
from aries.stt import SpeechToText
import os
import time

def main():
    # Initialize memory and speech modules
    memory = load_memory()
    tts = TextToSpeech()
    stt = SpeechToText()

    print("🤖 Aries is ready. Type or press Enter to talk (say 'exit' to quit).")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            # Voice input
            print("🎤 Listening...")
            user_input = stt.record_and_transcribe(duration=5)
            if not user_input:
                print("Didn't catch that, try again.")
                continue
            print(f"You (voice): {user_input}")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Build prompt with memory and get AI response
        prompt = build_prompt_with_memory(user_input, memory)
        print("\n[Asking Aries...]\n")
        ai_raw = mistral_chat(prompt)
        ai_clean = clean_ai_text(ai_raw)

        print("AI:", ai_clean)
        tts.speak(ai_clean)  # Convert AI text to speech

        # Save to memory
        memory.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "input": user_input,
            "output": ai_clean
        })
        save_memory(memory)

if _name_ == "_main_":
    main()
