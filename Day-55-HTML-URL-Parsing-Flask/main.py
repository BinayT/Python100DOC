from flask import Flask
app = Flask(__name__)


def make_bold(fun):
    def make_boldd():
        return f'<b>{fun()}</b>'
    return make_boldd


def make_emphasis(fun):
    def make_emphasiss():
        return f'<em>{fun()}</em>'
    return make_emphasiss


def make_underlined(fun):
    def make_underlinedd():
        return f'<u>{fun()}</u>'
    return make_underlinedd


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello, World!'


@app.route('/<namee>')
def say_hello(name):
    return f'Helloo, {name}!'


if __name__ == '__main__':
    app.run(debug=True)