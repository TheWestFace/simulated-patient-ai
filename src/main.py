from audio.record import record_audio
from audio.speech_to_text import transcribe
from audio.text_to_speech import speak
from patient.simulator import get_patient_response

print("=" * 50)
print("🎭 Welcome to the Simulated Patient AI Training")
print("Instructions:")
print("  - Press ENTER to start speaking")
print("  - Speak to the patient after the beep")
print("  - Type 'Q' and press ENTER anytime to quit")
print("=" * 50)

while True:

    user_input = input("\nPress ENTER to talk or type 'Q' to quit: ").strip().upper()

    if user_input == "Q":
        print("=" * 50)
        print("Exiting simulation. Goodbye!")
        break

    audio_file = record_audio()

    text = transcribe(audio_file)

    print("\nYou:", text)

    response = get_patient_response(text)

    speak(response)
