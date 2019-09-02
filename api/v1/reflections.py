from flask_restful import Api, Resource, reqparse, fields, marshal
from flask import Flask, url_for, request, abort, make_response, jsonify
from constant import *
from model import db
import sys
import json


class ReflectionAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # works for body parameters when set as json...1a & both 1a and 1b must be present i.e. not commented out
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No title is provided', location='json')

        # self.reqparse.add_argument('price', type=str, location='json')
        # self.reqparse.add_argument('done', type=bool, location='json')
        super(ReflectionAPI, self).__init__()

    def get(self, id=None):
        if not id:
            db.query(FIND_ALL, "")
        else:
            db.query(FIND_BY_ID, id)

    def post(self, id=None):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('success', type=str, required=True, help='No success is provided', location='json')
        self.reqparse.add_argument('low_point', type=str, required=True, help='No low_point is provided',
                                   location='json')
        self.reqparse.add_argument('take_away', type=str, required=True,
                                   help='No title is provided', location='json')
        values = self.reqparse.parse_args()
        db.query(CREATE, values)

    def put(self, id=None):
        if not id:
            return make_response(jsonify({"error": "id should be provided"}), 400)
        else:
            # db.query(FIND_BY_ID, id)

            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('success', type=str, required=True, help='No success is provided',
                                       location='json')
            self.reqparse.add_argument('low_point', type=str, required=True, help='No low_point is provided',
                                       location='json')
            self.reqparse.add_argument('take_away', type=str, required=True,
                                       help='No title is provided', location='json')
            values = self.reqparse.parse_args()
            # logger(values)
            response = db.query(UPDATE_BY_ID, values)

            # it works finally
            return json.loads(json.dumps(response["data"])), response["status"]

    def delete(self, id=None):
        if not id:
            # response = jsonify({"error": "id should be provided"})
            # response.status_code = 400
            return make_response(jsonify({"error": "id should be provided"}), 400)  # or response
        else:
            db.query(DELETE_BY_ID, id)


def logger(logs):
    sys.stdout.write(str(logs) + '\n')
