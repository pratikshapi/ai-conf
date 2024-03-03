from pydub import AudioSegment

audio = AudioSegment.from_file("audio.wav")
reversed_audio = audio.reverse()
reversed_audio.export("audio_reversed.wav", format="wav")
