from flask import Flask, render_template, request, flash, g
import os
import sqlite3
from fdatabase import FDataBase

DATABASE = 'flsk.db'
DEBUG = True
SECRET_KEY = 'b7bed93a911b960fe4da1aa39bbed836d22f88f6'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE = os.path.join(app.root_path, 'flsk.db'))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def clos_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()

# from dwa.site_db import create_db
# create_db()
