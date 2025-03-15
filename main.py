from flask import Flask, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_pod_number():
    return os.getenv("POD_NUMBER", "UNKNOWN")

@app.route('/')
def index():
    logger.info('Received request to /')
    return 'Welcome to the Flask application! Try /pod1, /pod2, or /pod3 endpoints.'

@app.route('/pod1')
def pod1():
    logger.info('Received request to /')
    return f'Hello, World! from pod {get_pod_number()}'

@app.route('/pod2')
def pod2():
    logger.info('Received request to /')
    return f'Hello, World! from pod {get_pod_number()}'

@app.route('/pod3')
def pod3():
    logger.info('Received request to /')
    return f'Hello, World! from pod {get_pod_number()}'

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
