from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home_page():
        return render_template('create.html')

    @app.route('/puzzle')
    def puzzle_page():
        return 'Puzzle created!'

    @app.route('/gallery')
    def gallery_page():
        return 'Gallery'

    @app.route('/puzzle/<puzzle_id>')
    def play_puzzle_page(puzzle_id):
        return 'Play'

    return app
