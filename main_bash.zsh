#!/bin/zsh

# Set the capture file name and path
capture_file="/tmp/network_capture.pcap"

echo "Starting network traffic capture. Press Ctrl+C to stop."

# Capture network traffic using tcpdump with options to capture all interfaces
# and save it to the specified file.
# Adjust the capture filter and other options as needed.
tcpdump -i any -w "$capture_file" &

# Store the PID of the tcpdump process
tcpdump_pid=$!

# Wait until the capture file is created (indicating tcpdump is running)
while [ ! -f "$capture_file" ]; do
    sleep 1
done

# Wait for SIGINT signal (Ctrl+C) to stop the capture
trap "cleanup" INT
cleanup() {
    echo "Stopping the capture..."
    kill $tcpdump_pid
    exit 0
}

# Wait indefinitely to keep the script running until the capture is stopped
while true; do
    sleep 1
done
