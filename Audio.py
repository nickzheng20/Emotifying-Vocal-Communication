import sounddevice as sd
import numpy as np
import soundfile as sf
import os
import noisereduce as nr

import tkinter as tk
from tkinter import filedialog
def record_audio():
    global recording, is_recording
    fs = 44100  # Sampling rate
    duration = 3  # Duration in seconds

    if not is_recording:
        is_recording = True
        recording_button.config(text='Stop Recording')
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
        sd.wait()
        recording = nr.reduce_noise(y=recording[:, 0], sr=fs)
        is_recording = False
        recording_button.config(text='Start Recording')
        print("Recording finished. Noise reduced.")
    else:
        sd.stop()
        is_recording = False
        recording_button.config(text='Start Recording')


def save_audio():
    directory = 'Audios/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "test_sound.wav"
    file_path = os.path.join(directory, filename)
    
    print(f"Saving recording to {file_path}...")
    sf.write(file_path, recording, 44100)
    print("Recording saved.")

def play_audio():
    if recording is not None:
        print("Playing audio...")
        sd.play(recording, samplerate=44100)
        sd.wait()
        print("Playback finished.")