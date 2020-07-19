from ..api import api  # noqa
from ..main import app
from flask import render_template


@app.route("/")
def home():
    # currency converter frontend
    return render_template('index.html')
