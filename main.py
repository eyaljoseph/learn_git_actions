from flask import Flask, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

POD_NUMBER = os.getenv("POD_NUMBER", "UNKNOWN")

@app.route('/')
def hello_world():
    logger.info('Received request to /')
    return f'Hello, World! from pod {POD_NUMBER}'

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
