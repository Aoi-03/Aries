from aries.memory import load_memory, save_memory
from aries.utils import build_prompt_with_memory, clean_ai_text
from aries.llm import mistral_chat
from aries.speech import record_audio, transcribe_audio, kokoro_speak
import os
import time

def main():
    memory = load_memory()
    print("Aries is ready. Type or press Enter to talk (say 'exit' to quit).")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            audio_file = os.path.join("temp_audio", "temp.wav")
            record_audio(filename=audio_file)
            user_input = transcribe_audio(audio_file)
            if not user_input:
                print("Didn't catch that, try again.")
                continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        prompt = build_prompt_with_memory(user_input, memory)
        print("\n[Asking Aries...]\n")
        ai_raw = mistral_chat(prompt)
        ai_clean = clean_ai_text(ai_raw)
        print("AI:", ai_clean)

        kokoro_speak(ai_clean)

        memory.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "input": user_input,
            "output": ai_clean
        })
        save_memory(memory)

if _name_ == "_main_":
    main()
