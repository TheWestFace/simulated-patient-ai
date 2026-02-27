from faster_whisper import WhisperModel

model = WhisperModel("base")


def transcribe(audio_file):

    segments, _ = model.transcribe(audio_file)

    text = " ".join([seg.text for seg in segments])

    return text
