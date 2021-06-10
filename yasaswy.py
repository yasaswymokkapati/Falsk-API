from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route('/')

def index():
    return jsonify({
        'data' : data,
        'message' : 'success'
    }), 200

@app.route('/star')

def planet():
    name = request.args.get('Star_name.1')
    planet_data = next(item for item in data
    if item['Star_name.1'] == name)
    return jsonify({
        'data' : planet_data,
        'message' : 'success'
    }), 450

if __name__ == '__main__':
    app.run()