from flask import Flask, render_template, g
import requests
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "money.db")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path)
    return db

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    cur = get_db().cursor()
    cur.execute("""SELECT * FROM 'money'; """)
    items = cur.fetchall()
    
    return render_template('index.html', items=items)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
