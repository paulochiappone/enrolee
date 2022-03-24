from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.events import Event

@app.route("/new-event")
def index():
    return render_template('new_event.html')


