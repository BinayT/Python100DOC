from flask import Flask
from random import randint
app = Flask(__name__)

random_number = randint(0, 10)


def h1_tag(fun):
    def return_h1():
        return f'<h1>{fun()}</h1>'
    return return_h1


@app.route('/')
@h1_tag
def home_page():
    return f'Welcome to higher lower game!<p>Shhh! The number is {random_number}</p>'


@app.route(f'/<int:number>')
@h1_tag
def right_page(number):
    if number == random_number:
        return 'You Found me<br/><img src="https://icons-for-free.com/iconfiles/png/512/correct+mark+success+tick+' \
               'valid+yes+icon-1320167819078544687.png" width=200 />'
    elif number > random_number:
        return 'Litter lower<br/><img src="https://cdn0.iconfinder.com/data/icons/arrows-2-10/128/Download-Arrow' \
               '-Downloader-Descend-Downward-Lower-Drop-512.png" width=200 />'
    else:
        return 'Litter upper<br/><img src="https://cdn4.iconfinder.com/data/icons/variety-of-arrows/32/arrows-35-512.png" ' \
               'width=200 />'


if __name__ == '__main__':
    app.run(debug=True)