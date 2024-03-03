import cv2

# Load the video
video_path = 'vid.mp4'
cap = cv2.VideoCapture(video_path)

# Frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Interval for frame extraction (1 frame every second)
interval = int(fps) 

frame_count = 0
saved_frame_count = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # Save frame every 'interval' frames
    if frame_count % interval == 0:
        cv2.imwrite(f"frame_{saved_frame_count}.jpg", frame)
        saved_frame_count += 1

    frame_count += 1

cap.release()
