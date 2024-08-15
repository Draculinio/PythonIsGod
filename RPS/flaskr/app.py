import os
from flask import Flask, jsonify, request
import logging
from rps import Rps
from db_manager import Db_manager

app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def index():
    return '<p>ROCK, PAPER, SCISSORS IN THE ALMIGHTY PYTHON</p>'

@app.route('/play', methods=['POST'])
def play():
    try:
        if request.json['move'] not in ['rock', 'paper','scissors']:
            return jsonify({'message':'Invalid move'})

        rps = Rps()
        app.logger.debug('here')
        (move,result) = rps.play(request.json['move'])
        
        return jsonify({
            'message':result,
            'move': move
        })
    except Exception as e:
        return jsonify({'error':str(e)})

@app.route('/statistics', methods=['GET'])
def statistics():
    db_manager = Db_manager()
    stats = db_manager.get_statistics()
    return jsonify(stats)

if __name__ == '__main__':
    app.run()