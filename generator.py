import os
import cv2
import time
import pathlib
import numpy as np

# Video properties
frame_width = 640
frame_height = 480
frame_rate = 1
video_duration = 30  # in seconds
circle_radius = 6

# Main loop
while True:
    start_time = int(time.time() * 1000)  # current time in milliseconds
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    filename = f'{start_time}.mp4'
    video = cv2.VideoWriter(filename, fourcc, frame_rate, (frame_width, frame_height))
    end_time = start_time + (video_duration * 1000)  # 30 seconds later

    # Generate random position for the circle
    center = (np.random.randint(0, frame_width), np.random.randint(0, frame_height))

    print(f'Generating video for {video_duration} seconds: final file name {filename}')

    while int(time.time() * 1000) < end_time:
        # Create a blank image
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

        cv2.circle(frame, center, circle_radius, (0, 255, 0), -1)

        # Add timestamp
        timestamp_text = f'{int(time.time() * 1000)} ms'
        cv2.putText(frame, timestamp_text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Write the frame
        video.write(frame)

        # Delay to match the frame rate
        time.sleep(1 / frame_rate)

    video.release()

    # uncomment if using continuous files
    # pathlib.Path.rename(filename, f'stream/{filename}') 
    # uncomment if using static file replaced everytime
    # pathlib.Path.rename(filename, f'stream/input.mp4')