# rtsp-streaming

# Install gst-rtsp-server (example for Ubuntu)
sudo apt-get install libgstrtspserver-1.0-0 gstreamer1.0-rtsp

# Sample command to run an RTSP server
# This command might vary based on your installation and needs
test-launch "( videotestsrc ! x264enc ! rtph264pay name=pay0 pt=96 )"