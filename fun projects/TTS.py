import pyaudio
from gtts import gTTS
import tempfile
import os
import webbrowser

text = "Hello! Why do you want pizda, horosho pizda? Maybe you should have a penis."

def do_tts(text):
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(temp_file.name)
    file_path = os.path.abspath(temp_file.name)
    temp_file.close()
    return file_path

file_path = do_tts(text)

# Use a web browser to play the audio file
webbrowser.open("file://" + file_path)

# Cleanup: Remove the temporary file
os.remove(file_path)
