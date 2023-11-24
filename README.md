# rtsp-streaming

# Install gst-rtsp-server (example for Ubuntu)
sudo apt-get install libgstrtspserver-1.0-0 gstreamer1.0-rtsp

# Sample command to run an RTSP server
# This command might vary based on your installation and needs
test-launch "( videotestsrc ! x264enc ! rtph264pay name=pay0 pt=96 )"



I want to try running the RTSP server in a docker image to make it easier for me to run this on a MacBook that uses architectre arm64. I want run all of my scripts in separate services using docker compose. What I want is to use generator.py to generate the video files in the stream/ folder in the host and map that as a volume that is visible to all other docker images in the same docker compose structure. 

This is the tree structure I have:

── LICENSE
├── README.md
├── ffmpeg
├── generator.py
├── requirements.txt
├── stream
│   └── no-delete
└── streamer-rtsp.py

The streamer-rtsp.py script takes files in the stream/ folder and sends it out to the rtsp server we are about to create.

Can you help me with that?
