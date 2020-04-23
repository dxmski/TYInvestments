from flask import Flask
from flask import render_template
from functions import create_table, insert_table, view_table
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
