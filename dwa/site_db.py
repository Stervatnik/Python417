from flask import Flask, render_template, request, flash
import os
import sqlite3

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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=[])


if __name__ == '__main__':
    app.run()

# from dwa.site_db import create_db
# create_db()
# 2:13 Остановился