from flask import Flask, render_template, request, flash, redirect, url_for

from puzzle import validate_list, create_puzzle


# constant values

CUSTOM_LIST = 0
AI_LIST     = 1
RANDOM_LIST = 2


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'tralalero tralala'

    @app.route('/', methods=['GET'])
    def create():
        return render_template('create.html')

    @app.route('/new', methods=['POST'])
    def new():
        list_type = request.form['type']
        text = request.form['text']

        try:
            list_type = int(list_type)
        except Exception as e:
            flash('An error occurred.', 'error')
            return redirect(url_for('create'))

        if list_type == CUSTOM_LIST:
            word_list = text.splitlines()
            message = validate_list(word_list)

            if message:
                flash(message, 'error')
                return redirect(url_for('create'))

        puzzle = create_puzzle(word_list)

        return render_template('new.html', puzzle=puzzle, link='wordsearch.io/d9Op2')

    @app.route('/gallery')
    def gallery():
        return 'Gallery'

    @app.route('/puzzle/<puzzle_id>')
    def puzzle(puzzle_id):
        return 'Play'

    return app
