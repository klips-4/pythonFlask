from flask import request
from app import app

from classes.EndpointFactory import EndpointFactory\


@app.route('/service', methods=['POST'])
def main_route():
    request_data = reuest.get_json() or {}
    return EndpointFactory(request_data).process()
