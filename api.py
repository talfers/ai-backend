import os
import json
from log import logging
from flask import Flask, request
from config import Config
from ai import AI


# Create app var from Flask package
server = Flask(__name__)
# Set path of current app dirname
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('api.py')

config = Config()
ai = AI(config.openai_key)


# Troubleshooting route
@server.route('/')
def home_route():
    response = { "msg": "welcome to the landlord assistant application" }
    res = server.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


# Director route
@server.route('/direct', methods=['POST'])
def director_route():
    try:
        # {"system_msg": str, "user_ai_msgs": list}
        response_object = ai.process_request(request)
        res = server.response_class(response=json.dumps(response_object), status=200, mimetype='application/json')
        logger.info("Successfully returned message.")
    except Exception as e:
        res = server.response_class(response=json.dumps({'text': f'Error sending model definitions. Error: {str(e)}'}), status=200, mimetype='application/json')
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res