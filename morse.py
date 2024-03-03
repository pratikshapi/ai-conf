from scipy.io import wavfile
from scipy.signal import find_peaks
import numpy as np

# Load the audio file
sample_rate, audio_data = wavfile.read('audio.wav')

# Ensure audio is mono
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)

# Normalize the audio to the range [-1, 1]
audio_data = audio_data / np.max(np.abs(audio_data))

# Find peaks in the audio signal
peaks, _ = find_peaks(audio_data, height=0.5)  # Threshold may need adjustment

# Convert peaks to time
times = peaks / sample_rate

# Find the duration between peaks
durations = np.diff(times)

# Determine the shortest duration, which likely corresponds to a dot
dot_duration = np.min(durations)

# Assume dash is three times the dot
dash_duration = dot_duration * 3

# Decode the durations into dots, dashes, and spaces
morse_code = ''
for duration in durations:
    if duration < dot_duration * 1.5:
        morse_code += '.'
    elif duration < dash_duration * 1.5:
        morse_code += '-'
    else:
        morse_code += ' '

# Dictionary to translate Morse code to letters
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

# Function to decode Morse code to text
def decode_morse(morse_code, morse_dict):
    words = morse_code.split('   ')  # Morse code words are separated by 3 spaces
    decoded_message = ''
    for word in words:
        for symbol in word.split():
            decoded_message += morse_dict.get(symbol, '')  # Translate symbol to letter
        decoded_message += ' '  # Add space between words
    return decoded_message.strip()

# Decode the Morse code into English text
decoded_message = decode_morse(morse_code, morse_dict)
print(decoded_message)
