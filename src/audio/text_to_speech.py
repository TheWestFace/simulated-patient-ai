import pyttsx3

engine = pyttsx3.init()


def speak(text):

    print("\nPatient:", text)

    engine.stop()

    engine.say(text)

    engine.runAndWait()
