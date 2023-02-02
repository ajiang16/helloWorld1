from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Amy Jiang! I am adding my first code change.'

@app.route('/Hello')
def hello():
    return render_template('Hello.html')

if __name__ == '__main__':
    app.run()
