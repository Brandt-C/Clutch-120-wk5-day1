from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/home')
def home():
    return {
        'Welcome home': 'there is no place like here'
    }

@app.route('/test')
def test():
    return {
        'Is this mic on?': 'is this function working????'
    }

