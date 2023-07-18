# Capture Traffic

## Overview

Capture Traffic is a simple Flask application that allows you to start and stop capturing network traffic using `tcpdump`. It provides two endpoints to control the capture process remotely.

## Endpoints
  /start_capture: Start capturing network traffic using tcpdump.
  /stop_capture: Stop the ongoing network traffic capture gracefully.

## Usage
Run the Flask application with elevated privileges (for tcpdump):
`sudo python3 main.py`
Access the following endpoints in your web browser or using tools like curl or httpie:

`http://127.0.0.1:5000/start_capture`: Start capturing network traffic.
`http://127.0.0.1:5000/stop_capture`: Stop the network traffic capture.
The application will print the captured traffic to /tmp/network_capture.pcap. You can access the captured data there.
