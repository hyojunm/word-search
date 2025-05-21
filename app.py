from flask import Flask, render_template, request

from puzzle import create_puzzle, print_puzzle


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET'])
    def create():
        return render_template('create.html')

    @app.route('/new', methods=['POST'])
    def new():
        word_list_type = request.form['word-list-type']
        word_list = request.form['word-list'].splitlines()

        puzzle = create_puzzle(word_list)

        if puzzle != None:
            print_puzzle(puzzle)

        return render_template('new.html', puzzle=puzzle, link='wordsearch.io/d9Op2')

    @app.route('/gallery')
    def gallery():
        return 'Gallery'

    @app.route('/puzzle/<puzzle_id>')
    def puzzle(puzzle_id):
        return 'Play'

    return app
