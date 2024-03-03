from moviepy.editor import VideoFileClip


video_path = 'vid.mp4'
audio_output_path = 'audio.wav'

video = VideoFileClip(video_path)
audio = video.audio

# Save the audio as a WAV file
audio.write_audiofile(audio_output_path, codec='pcm_s16le')

# Release resources
audio.close()
video.close()
