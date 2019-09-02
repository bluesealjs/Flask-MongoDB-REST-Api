from flask_restful import Api, Resource, reqparse, fields, marshal
from flask import Flask, url_for, request, abort, make_response, jsonify
from constant import *
from model import db
import sys


class ReflectionAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # works for body parameters when set as json...1a & both 1a and 1b must be present i.e. not commented out
        # self.reqparse.add_argument('title', type=str, required=True,
        #                            help='No title is provided', location='json')

        # self.reqparse.add_argument('price', type=str, location='json')
        # self.reqparse.add_argument('done', type=bool, location='json')
        super(ReflectionAPI, self).__init__()

    def get(self, data=None):
        params = data
        # logger(params)
        if data:
            db.query(FIND_ALL, "")
        else:
            db.query(FIND_BY_ID, params)

    def post(self, data=None):
        params = data
        # logger(params)
        if data:
            db.query(CREATE, params)

    def put(self, data=None):
        params = data
        # logger(params)
        if data:
            db.query(UPDATE_BY_ID, params)

    def delete(self, data=None, id=None):
        # logger(request.form['data'].title)
        params = data

        # works for body parameters when set as json ...1b
        # if 1a is commented out it prints '{}'
        logger(self.reqparse.parse_args())

        # works for body parameters when set as form-data ...2b
        # logger(request.form['title'])

        # works for when set as ../api/v1/<data> ....3b
        # logger(data)

        # works for when set as ../api/v1/<data>/<int:id> ....4b
        # logger(data + ", " + str(id))

        # works for when set as query parameters i.e. author:Kat ...5b
        # if 'author' not found it prints 'None'
        # logger(request.args.get('author'))
        # if not request.args.get('author'):
        #     logger("author value field is empty")
        # else:
        #     logger(request.args.get('author'))

        # if data:
        #     logger(data)
        #     # db.query(DELETE_BY_ID, params)
        # if id:
        #     logger(id)
        #     # db.query(DELETE_BY_ID, params)


def logger(logs):
    sys.stdout.write(str(logs) + '\n')
