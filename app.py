from flask import Flask, render_template

app = Flask(__name__)





@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/git_tutorial/')
def git_tutorial():
    return render_template('git_tutorial.html')


if __name__ == '__main__':
    app.run()
