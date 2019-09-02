import os
from api.v1.reflections import ReflectionAPI
from flask import Flask, url_for, request, abort, make_response, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal
from threading import Thread
import sys
import traceback

app = Flask(__name__)
api = Api(app)

value_of_x = None

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


api.add_resource(ReflectionAPI, '/api/v1/reflection', '/api/v1/reflection/', '/api/v1/reflection/<id>',
                 '/api/v1/reflection/<string:data>/<int:id>')


def logger(logs):
    sys.stdout.write(str(logs) + '\n')


# def init():
#     # global function
#     global value_of_x
#     value_of_x = "value of x is 55"
#     logger("value_of_x" + value_of_x)


if __name__ == '__main__':
    app.debug = True
    # Thread(target=init_func).start()
    # init()
    app.run(port=int(os.environ.get('PORT', 5000)))
