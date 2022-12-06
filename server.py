from flask import Flask
from random import randint


app = Flask(__name__)
random_choice = randint(1, 9)
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:Guess_the_numbers>')
def guess_random_number(Guess_the_numbers):
    if Guess_the_numbers == random_choice:
        return '<h1>you found me</h1>'\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    elif Guess_the_numbers > random_choice:
        return "<h1>Too high , try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>Too low, try again!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

if __name__ == '__main__':
    app.run(debug=True)