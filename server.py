import os
from flask import Flask, url_for, request, abort, make_response, jsonify
from threading import Thread
import sys
import traceback

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'blue':
        return 'seal'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


app = Flask(__name__)


def init():
    # global function
    init_func()


def init_func():
    logger("init func is called")


def logger(logs):
    sys.stdout.write(str(logs) + '\n')


value_of_x = None


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1', methods=['GET'])
def home():
    # print("home loaded", flush=True)
    global value_of_x
    value_of_x = "value of x is 55"
    return jsonify({'message': "hello from server", "value_of_x": value_of_x})


@app.route('/api/v1/post', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    message = request.json['title']
    return jsonify({'message': message}), 201


@app.route('/api/v1/put', methods=['PUT'])
def update_task():
    message = request.json['title']
    if len(message) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    message = request.json['title']
    return jsonify({'message': message}), 201


@app.route('/api/v1/<int:id>', methods=['GET'])
def home_id(id):
    # print("home loaded", flush=True)
    if id == 0:
        abort(404)
    global value_of_x
    value_of_x = id
    return jsonify({'message': "hello from server", "value_of_x": value_of_x})


@app.route('/api/v1/db', methods=['POST'])
def db():
    logger('this is inside db()')
    if request.method == 'POST':
        if value_of_x:
            try:
                comment = request.form['comment']
                my_prediction = "lorem ipsum"
                comment = "lorem ipsum comment"
                return jsonify({value_of_x})

            except:
                info = jsonify({'trace': traceback.format_exc()})
                return jsonify({info})
        else:
            # set value of x if not set yet
            logger('else block')
            info = "else block"
            return jsonify({info})


if __name__ == '__main__':
    app.debug = True
    # Thread(target=init_func).start()
    init()
    app.run(port=int(os.environ.get('PORT', 5000)))
