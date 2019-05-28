import os
from flask import Flask
from flask import request
from flask import json
from flask import jsonify
from gkb import get_keys
from gkb import set_values
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/keys')
def keys():
    results = '\n'.join(get_keys())
    return results

@app.route('/api/set_values', methods=['POST'])
def api_set_values():
    posted = request.get_json()
    keys = poested.keys()
    if len(keys) != 1:
        return jsonify({'Error': 'Specify only one key'})
    key = keys[0]
    values = posted[key]
    if type(values) != list or any(type(value) != str for value in values):
        return jsonify({'Error': 'Value must be an array of strings'})
    if set_values(key, values):
        values = get_values(key)
        return jsonify({key: values})
    else
        return jsonify({'Error': 'Failed to connect to Database'})

if __name__ == '__main__':
    app.run()
