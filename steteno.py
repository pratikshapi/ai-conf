import wave

def read_least_significant_bits(wav_filename):
    with wave.open(wav_filename, 'rb') as wav:
        length = wav.getnframes()
        audio_data = wav.readframes(length)
    
    # Assuming audio data is 16-bit samples
    hidden_bits = [frame & 1 for frame in audio_data]
    return hidden_bits

# Usage
hidden_data = read_least_significant_bits('audio.wav')
print(hidden_data)  # Printing first 100 bits of hidden data
