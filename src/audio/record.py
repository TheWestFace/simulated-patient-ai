import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(filename="input.wav", seconds=5):

    fs = 16000

    print("Speak now...")

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)

    sd.wait()

    write(filename, fs, recording)

    return filename
