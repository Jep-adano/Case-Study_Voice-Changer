import numpy as np
import librosa
import soundfile as sf
  
# Load the audio file
input_file, sr = librosa.load('/content/drive/MyDrive/DSP/ADANO (1).wav', sr=None)

# Adjust the pitch (n_steps) to control the pitch change
n_steps = -3
modified_audio = librosa.effects.pitch_shift(audio_file, n_steps=n_steps, sr=sr)

# Save the processed audio as a WAV file
output_file = '/content/drive/MyDrive/DSP/ADANO (1).wav'
sf.write(output_file, modified_audio, sr)

# Print a message to confirm the completion of the processing
print(f"Processed audio saved as {output_file}")
