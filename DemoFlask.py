from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def fun():
    return 'hello abhilash'

@app.route('/second')
def fun1():
    return '<h1>This is the second page</h1>'

@app.route('/third/<user>')
def fun2(user):
    return 'hello '+user

if __name__ == '__main__':
    app.run(host='0.0.0.0')
