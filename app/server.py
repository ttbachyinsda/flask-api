from flask import Flask  
from flask.sqlalchemy import SQLAlchemy  
import os  
from flask.login import LoginManager  
app=Flask(__name__)  
app.config.from_object('config')  
db=SQLAlchemy(app)  
lm = LoginManager()  
lm.init_app(app)  
lm.login_view = 'login'  
from app import views,models  