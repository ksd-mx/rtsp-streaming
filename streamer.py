import os
import requests
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VideoOutputWatcher(FileSystemEventHandler):
    def on_created(self, event):
        print('event created', event)
        if event.is_directory:
            return
        if event.src_path.endswith('.mp4'):
            self.process_video(event.src_path)

    def process_video(self, video_path):
        print('processing video', video_path)
        # Convert MP4 to RTSP using ffmpeg
        rtsp_stream_url = self.convert_to_rtsp(video_path)
        # Push to API
        # self.push_to_api(rtsp_stream_url)

    def convert_to_rtsp(self, video_path):
        # Define the RTSP stream URL (adjust according to your server setup)
        rtsp_stream_url = "rtsp://0.0.0.0:8554/test"
        # Command to use ffmpeg to stream the video to the RTSP server

        ffmpeg_command = [
            'ffmpeg',
            '-re',
            '-i', video_path,
            '-c:v', 'copy',
            '-c:a', 'copy',
            '-f', 'rtsp',
            rtsp_stream_url
        ]

        # Start the ffmpeg process in the background
        subprocess.Popen(ffmpeg_command)

        # Return the RTSP stream URL
        return rtsp_stream_url

def main():
    path = "stream/"
    event_handler = VideoOutputWatcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        print('Watching for new videos...')
        while True:
            # Run indefinitely
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
