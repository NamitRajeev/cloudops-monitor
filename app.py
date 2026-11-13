
from flask import Flask, jsonify
from datetime import datetime, timezone
import platform
import os

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route("/")
def home():
    return jsonify({
        "application": "CloudOps Monitor",
        "version": APP_VERSION,
        "status": "Running",
        "message": "Welcome to our DevOps project!"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route("/system")
def system():
    return jsonify({
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "python_version": platform.python_version(),
        "process_id": os.getpid()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False) #.\venv\Scripts\Activate.ps1

