from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from CI/CD Pipeline!",
        "status": "running",
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/info')
def info():
    return jsonify({
        "app": "Simple Python App",
        "version": "1.0.0",
        "platform": platform.system(),
        "python_version": platform.python_version()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
