from song_preview import get_song_preview
import requests
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import tempfile

#Search for the audio file
audio_url = get_song_preview("Hold me down Daniel Ceaser")
print(audio_url)

#Download the audio file
response = requests.get(audio_url)

#Save the file temporarily
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
    temp_audio_file.write(response.content)
    temp_audio_path = temp_audio_file.name

#Load the audio file with librosa
y, sr = librosa.load(temp_audio_path)

#Generate a Mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
S_db = librosa.power_to_db(S, ref=np.max)



#Plot the spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title("Mel Spectrogram")
plt.xlabel("Time")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()


