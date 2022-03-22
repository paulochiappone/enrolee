from flask import jsonify, render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
# from flask_app.models.events import Event
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template('index.html')