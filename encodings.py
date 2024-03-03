import numpy as np
from scipy.io import wavfile
from scipy.signal import find_peaks

# Load audio file
sample_rate, data = wavfile.read('audio.wav')

# Convert to mono if stereo
if data.ndim > 1:
    data = data.mean(axis=1)

# Normalize data
data = data / np.max(np.abs(data))

# Find peaks to identify beeps
peaks, _ = find_peaks(data, height=0.5)  # adjust height as needed

# Assuming a fixed tone length for dots and a triple length for dashes
dot_length = np.min(np.diff(peaks))  # Minimum distance between peaks as dot length
dash_length = 3 * dot_length  # Adjust as necessary

# Decode Morse code (simplified and needs refinement for a real application)
morse_code = ""
for i in range(len(peaks)-1):
    duration = peaks[i+1] - peaks[i]
    if duration <= dot_length * 1.5:
        morse_code += "."
    elif duration <= dash_length * 1.5:
        morse_code += "-"
    else:
        morse_code += " "  # Space between letters or words

print(morse_code)
