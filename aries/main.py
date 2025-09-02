from aries.architecture import AriesArchitecture
from config import CONFIG  # We'll create this next

def main():
    # Initialize Aries
    aries = AriesArchitecture(CONFIG)
    aries.start()

    print("Aries is ready. Say something or type (type 'exit' to quit).")

    while True:
        user_input = input("You: ").strip()

        if not user_input:  # If no text input, listen for voice
            audio_data = aries.stt.listen()  # Returns {'text': ..., 'audio_path': ...}
            user_input = audio_data['text']

        if not user_input:
            print("Didn't catch that, try again.")
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Detect emotion from audio (optional)
        emotion = None
        if 'audio_path' in locals():
            emotion = aries.emotion.predict(audio_data['audio_path'])

        # Generate response using LLM
        response = aries.llm.generate(
            user_input,
            context=aries.memory.get_context()
        )

        print(f"Aries: {response}")

        # Speak response
        aries.tts.speak(response)

        # Store memory
        aries.memory.store(user_input, response, emotion)

    aries.stop()

if _name_ == "_main_":
    main()
