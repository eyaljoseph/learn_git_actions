import os
from flask import Flask

app = Flask(__name__)

POD_NUMBER = os.getenv("POD_NUMBER", "UNKNOWN")

@app.route('/')
def hello_world():
    return f"Hello, World! from pod {POD_NUMBER}"

@app.route('/check')
def check():
    return 'checking'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
