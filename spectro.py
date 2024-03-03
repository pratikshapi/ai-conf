import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

sampling_rate, data = wavfile.read('audio_reversed.wav')

if data.ndim > 1:
    data = np.mean(data, axis=1)

nperseg = min(len(data) // 8, 256) 

# Generate spectrogram with adjusted nperseg
frequencies, times, Sxx = spectrogram(data, fs=sampling_rate, nperseg=nperseg)

Sxx_modified = np.where(Sxx <= 0, 1e-12, Sxx)

plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx_modified), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram')
plt.colorbar(label='Intensity [dB]')
plt.show()
