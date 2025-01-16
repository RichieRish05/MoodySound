from song_preview import get_song_preview
import requests
import librosa
import librosa.display
import numpy as np
import tempfile

#Search for the audio file
audio_url = get_song_preview("Blank Space Taylor Swift")
print(audio_url)


def get_spectrogram_data(audio_url):
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
    

def generate_spectrograms_of_length_one_through_thirty(spectrogram):
    sr = 22050
    duration = 30
    # Number of time steps in the original spectrogram
    total_time_steps = spectrogram.shape[1]

    # Total duration of the original audio (in seconds)
    duration = 30

    # Calculate time steps per second
    time_steps_per_second = total_time_steps // duration

     # Initialize the list to store spectrograms
    spectrograms = []

    for i in range(1, duration + 1):  # Generate spectrograms for 1 to 30 seconds
        # Calculate the number of time steps corresponding to the current duration
        time_steps = time_steps_per_second * i

        # Slice the spectrogram to include only the required time steps
        audio_part = spectrogram[:, :time_steps]

        # Pad the remaining time steps with zeros to maintain consistent shape
        padding_steps = total_time_steps - time_steps
        padded_spectrogram = np.pad(audio_part, ((0, 0), (0, max(0, padding_steps))), mode='constant')

        # Append the resulting spectrogram to the list
        spectrograms.append(padded_spectrogram)

    return spectrograms


