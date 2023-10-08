import numpy as np
import librosa
import soundfile as sf

# Load the audio file
audio_file, sr = librosa.load('https://drive.google.com/drive/folders/1hvvOdu8HTsZr6YJgM_agMWqIRwLlgzxS?usp=drive_link', sr=None)

# Adjust the pitch (n_steps) to control the pitch change
n_steps = -3
shifted_audio = librosa.effects.pitch_shift(audio_file, n_steps=n_steps, sr=sr)

# Save the processed audio as a WAV file
output_file = '/content/drive/MyDrive/DSP/VILLASAN.wav'
sf.write(output_file, shifted_audio, sr)

# Print a message to confirm the completion of the processing
print(f"Processed audio saved as {output_file}")
