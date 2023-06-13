from app import app

from flask import render_template

@app.route('/')
def land():
    teachers = [
        {
            'name': 'Brendan',
            'subject': 'Front end stuff',
            'age' : 654
        },
        {
            'name' : 'Rachel',
            'subject': 'student relations',
            'age' : 980
        },
        {
            'name' : 'Brandt',
            'subject': 'lecture',
            'age' : 765
        }
    ]
    return render_template('index.html', teach_list=teachers)

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

