import os, shutil
FFMPEG_BIN = r"C:\Users\seeke\Downloads\ffmpeg-2025-11-02-git-f5eb11a71d-essentials_build\ffmpeg-2025-11-02-git-f5eb11a71d-essentials_build\bin"
os.environ["PATH"] += os.pathsep + FFMPEG_BIN
print("ffmpeg path:", shutil.which("ffmpeg") or "NOT FOUND")

import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from commands import commands
import re

print("Testing audio device...")
print(sd.query_devices())

fs = 44100  # sample rate

print("Recording..... Speak your command")
duration = 4  # seconds
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
write("cmd.wav", fs, recording)

print("Converting speech to text...")
model = whisper.load_model("base")
result = model.transcribe("cmd.wav")
text = result["text"].lower()
print("You said:", text)

# command matching
matched = False
clean_text = re.sub(r'[^a-zA-Z ]', '', text)

for phrase in commands:
    if phrase in clean_text:
        print("Cockpit Response:", commands[phrase])
        matched = True
        break

if not matched:
    print("Command not recognized. Try speaking clearer.")
