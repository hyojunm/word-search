from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Home'


@app.route('/puzzle')
def puzzle_page():
    return 'Puzzle created!'


@app.route('/gallery')
def gallery_page():
    return 'Gallery'


@app.route('/puzzle/<puzzle_id>')
def play_puzzle_page(puzzle_id):
    return f'Viewing puzzle {escape(puzzle_id)}'
