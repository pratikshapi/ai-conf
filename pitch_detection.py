import librosa
import numpy as np

# Load the audio file
audio_path = 'audio.wav'
y, sr = librosa.load(audio_path)

# Extract pitches and magnitudes
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Select out the dominant pitch for each time frame
# (This is a simplified approach and may need refinement for complex audio)
pitch_values = [pitches[:, i].argmax() for i in range(magnitudes.shape[1])]
dominant_pitches = [pitches[pitch_values[i], i] for i in range(len(pitch_values))]
dominant_pitches_hz = librosa.core.hz_to_midi(dominant_pitches)

# Map MIDI note numbers to note names
note_names = [librosa.midi_to_note(pitch) for pitch in dominant_pitches_hz]

# Print out the sequence of notes
# print(note_names)

# Now, if you have a cipher that maps notes to letters, you can apply it here
cipher = {'C': 'A', 'C#': 'B', 'D': 'C', 'D#': 'D', 'E': 'E', 'F': 'F', 'F#': 'G', 'G': 'H', 'G#': 'I', 'A': 'J', 'A#': 'K', 'B': 'L'}

# Decipher the message
deciphered_message = ''.join([cipher.get(note[:-1], '') for note in note_names])

print(deciphered_message)
