from flask_restful import Api, Resource, reqparse, fields, marshal
from flask import Flask, url_for, request, abort, make_response, jsonify
from constant import *
import sys


def query(operation, params):
    switcher = {
        CREATE: create,
        FIND_ALL: find_all,
        FIND_BY_ID: find_by_id,
        UPDATE_BY_ID: update_by_id,
        DELETE_BY_ID: delete_by_id
    }
    func = switcher.get(operation, "Oops! Error occurred")
    return func(params)


def create(params):
    logger("create, params: " + params)
    return jsonify({'message': "create, params: " + params})


def find_all(params):
    logger("find_all, params: " + params)
    return jsonify({'message': "find_all, params: " + params})


def find_by_id(params):
    logger("find_by_id, params: " + params)
    return jsonify({'message': "find_by_id, params: " + params})


def update_by_id(params):
    logger("update_by_id, params: " + params)
    return jsonify({'message': "update_by_id, params: " + params})


def delete_by_id(params):
    logger("delete_by_id, params: " + params)
    return jsonify({'message': "delete_by_id, params: " + params})


def logger(logs):
    sys.stdout.write(str(logs) + '\n')
