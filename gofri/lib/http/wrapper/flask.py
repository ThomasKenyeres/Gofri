from flask import Flask
from flask_restful import Api


class FlaskApplication:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)