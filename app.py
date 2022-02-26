import argparse
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-reload', action='store_true', default=False)
    args = vars(parser.parse_args())

    # Settings
    debug = True if args['no_reload'] else False

    # Execute
    app.run(debug=debug)
