from audio.record import record_audio
from audio.speech_to_text import transcribe
from audio.text_to_speech import speak
from patient.simulator import get_patient_response

while True:

    input("\nPress ENTER to talk")

    audio_file = record_audio()

    text = transcribe(audio_file)

    print("\nYou:", text)

    response = get_patient_response(text)

    speak(response)
