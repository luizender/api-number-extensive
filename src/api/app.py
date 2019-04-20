"""
This module has the App and Routes of API
"""
import json
import logging.config
from flask import Flask
from flask_restful import Api
from api.resources import NumberResource
from api.defines import LOGGING_FILE

# Create the API app
APP = Flask(__name__)
API = Api(APP)

# URLs of API
API.add_resource(NumberResource, '/', '/<string:number>')

if __name__ == '__main__':
    # set up proper logging.
    with open(LOGGING_FILE, "r", encoding="utf-8") as config:
        logging.config.dictConfig(json.load(config))
    APP.run(host='0.0.0.0', use_reloader=True)
