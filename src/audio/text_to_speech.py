import pyttsx3

# engine = pyttsx3.init()


def speak(text):

    print("\nPatient:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
