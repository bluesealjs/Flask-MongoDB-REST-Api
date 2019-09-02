import os
from flask import Flask, url_for, request
from flask import jsonify
from threading import Thread
import sys
import traceback

app = Flask(__name__)


def init():
    # global function
    init_func()


def init_func():
    logger("init func is called")


def logger(logs):
    sys.stdout.write(str(logs) + '\n')


value_of_x = None


@app.route('/')
def home():
    # print("home loaded", flush=True)
    global value_of_x
    value_of_x = "value of x is 55"
    return jsonify({'message': "hello from server", "value_of_x": value_of_x})


@app.route('/db', methods=['POST'])
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
