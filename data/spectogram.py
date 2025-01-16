from song_preview import get_song_preview
import requests
import librosa
import librosa.display
import numpy as np
import tempfile

#Search for the audio file
audio_url = get_song_preview("Dap You Up Speaker Knockerz")
print(audio_url)


def get_spectogram_data(audio_url):
    #Download the audio file
    response = requests.get(audio_url)

    # Save the file temporarily
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio_file:
        # Write the content of the audio file to the temporary file
        temp_audio_file.write(response.content)

        # Create a fake path for librosa to work with
        temp_audio_path = temp_audio_file.name

        # Load the temporary file with a predetermined sampling rate and a duration of 30 seconds to preprocess data
        sr=22050
        duration=30
        y, _ = librosa.load(temp_audio_path, sr=sr, duration=duration)
        target_length = sr * duration  # Target length in samples (30 seconds)

        if len(y) > target_length:
            y = y[:target_length]  # Trim to 30 seconds
        else:
            y = np.pad(y, (0, max(0, target_length - len(y))), mode='constant')  # Pad the end of the audio with zeros




        # Generate a Mel spectrogram
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)

        # Convert power to decibels
        S_db = librosa.power_to_db(S, ref=np.max)

        return S_db
    

data = get_spectogram_data(audio_url)
print(data.shape)






"""
#Plot the spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title("Mel Spectrogram")
plt.xlabel("Time")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()
"""


