from flask import Flask, jsonify
import subprocess
import signal
import os

app = Flask(__name__)

# Path to the bash script
bash_script_path = "/Users/yogeshdwivedi/demo_project/sample_bash.zsh"

# Variable to hold the process ID of the tcpdump process
capture_process = None


def start_capture():
    global capture_process

    if capture_process is not None:
        return jsonify({"message": "Traffic capture is already running."})

    try:
        # Start the tcpdump process in the background and store its PID
        capture_process = subprocess.Popen(["sudo", bash_script_path])
        return jsonify({"message": "Traffic capture started successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def stop_capture():
    global capture_process

    if capture_process is None:
        return jsonify({"message": "No traffic capture is currently running."})

    try:
        # Stop the capture by killing the previous background process
        subprocess.run(["pkill", "-SIGINT", "tcpdump"])
        return jsonify({"message": "Traffic capture stopped successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/start_capture', methods=['GET'])
def start_capture_endpoint():
    return start_capture()


@app.route('/stop_capture', methods=['GET'])
def stop_capture_endpoint():
    return stop_capture()


if __name__ == '__main__':
    app.run(debug=True)


