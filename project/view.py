# project / view.py

import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request, session, url_for

# config
app = Flask(__name__)
app.config.from_object('_config')


# helper functions
def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required():
    @wraps(test)
    def wrap(*args, **kwargs):
        if logged_in in session:
            return test(*args, **kwargs)
        else:
            flask('You need to login first')
            return redirect(url_for('login'))
    return wrap

# route handlers


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('Good bye')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.confg['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = "Invalid credentials"
            return render_template('login.html', error)
        else:
            session['logged_in'] = True
            flash('Welcome')
            return redirect(url_for('tasks'))
    return render_template('login.html')
