from flask_wtf import Form
from wtforms import TextField, BooleanField, FileField
from wtforms.validators import Required

class RegForm(Form):
    id = TextField('id', validators = [Required()])
    password = TextField('password', validators=[Required()])
    filename = FileField('filename', validators = [Required()])
class LoginForm(Form):
    id = TextField('id', validators = [Required()])
    password = TextField('password', validators=[Required()])
    
