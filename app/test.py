from flask import render_template, flash, redirect, session,request, url_for, Response, g ,Flask
from flask_login import login_user, logout_user, current_user, login_required
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64
import os

from forms import LoginForm, RegForm
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/getrawimage/<username>')
def getrawimage(username):
    image = open("./instance/{}.png".format(username), 'rb').read()
    resp = Response(image, mimetype="image/png")
    return resp

@app.route('/gettempimage/<username>')
def getrawimage(username):
    image = open("./instance/tempg/{}.png".format(username), 'rb').read()
    resp = Response(image, mimetype="image/jpeg")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=810)