from gtts import gTTS
import os

def text_to_speech(text, filename):

    os.makedirs("audio", exist_ok=True)

    filepath = os.path.join(
        "audio",
        filename
    )

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(filepath)

    return filepath