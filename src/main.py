from flask import Flask
import os
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return ("(animals can't talk, right?)", 200)


@app.route('/exhibit')
def ex():
    if os.getenv('IMGURL') is not None:
        return ('<img src="' + os.getenv('IMGURL') +
                '" height="25%" width="25%" />', 200)
    else:
        return ('<img src="https://zoologyfoundation.org/wp-content/uploads/woocommerce-placeholder.png" height="25%" width="25%" />', 200)


@app.route('/action')
def action():
    if os.getenv('NAME') is not None:
        name = os.getenv("NAME")
    else:
        name = 'animal'

    if os.getenv('ACTIONS') is not None:
        actionList = os.getenv('ACTIONS').split(',')
        random.seed()
        selection = random.randint(0, len(actionList)-1)
    else:
        return ('The animal is not visible right now.', 200)
    return ('The ' + name + ' ' + actionList[selection], 200)

