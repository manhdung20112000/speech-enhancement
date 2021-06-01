import os
import librosa
import librosa.display
import numpy as np
from matplotlib import pyplot as plt

def change_name(path):
    """Change the duplicate file name"""
    os.chdir(path)
    filenames = os.listdir()

    print(filenames)
    for dir in filenames:
        for file in os.listdir(dir):
            os.rename(dir+'/'+file, f'{dir}_{file}')

def plot_spectrogram(stftaudio_magnitude_db, sample_rate, hop_length_fft) :
    """This function plots a spectrogram"""
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(stftaudio_magnitude_db, x_axis='time', y_axis='linear',
                             sr=sample_rate, hop_length=hop_length_fft)
    plt.colorbar()
    title = 'hop_length={},  time_steps={},  fft_bins={}  (2D resulting shape: {})'
    plt.title(title.format(hop_length_fft,
                           stftaudio_magnitude_db.shape[1],
                           stftaudio_magnitude_db.shape[0],
                           stftaudio_magnitude_db.shape));
    return

def plot_time_serie(audio,sample_rate):
    """This function plots the audio as a time serie"""
    plt.figure(figsize=(12, 6))
    #plt.ylim(-0.05, 0.05)
    plt.title('Audio')
    plt.ylabel('Amplitude')
    plt.xlabel('Time(s)')
    librosa.display.waveplot(audio, sr=sample_rate)
    return