import argparse
from flask import Flask, render_template, request
from flask import session

from src.pipelines import count_frequencies

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    data = request.form
    user_string = data['String']
    char_freq = count_frequencies(user_string)

    return render_template('counts.html', string=user_string, char_freq=char_freq)


if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-reload', action='store_true', default=False)
    args = vars(parser.parse_args())

    # Settings
    debug = False if args['no_reload'] else True

    # Execute
    app.run(debug=debug)
