from flask_wtf import Form
from wtforms import TextField, BooleanField, FileField, IntegerField, FloatField
from wtforms.validators import Required

class RegForm(Form):
    id = TextField('id', validators = [Required()])
    password = TextField('password', validators=[Required()])
    filename = FileField('filename', validators = [Required()])
class LoginForm(Form):
    id = TextField('id', validators = [Required()])
    password = TextField('password', validators=[Required()])
class queryForm(Form):
    sym = IntegerField('sym', validators=[Required()])
    nor = IntegerField('nor', validators=[Required()])
    mak = TextField('mak', validators=[Required()])
    fue = TextField('fue', validators=[Required()])
    asp = TextField('asp', validators=[Required()])
    nod = TextField('nod', validators=[Required()])
    bod = TextField('bod', validators=[Required()])
    dri = TextField('dri', validators=[Required()])
    eng = TextField('eng', validators=[Required()])
    whe = FloatField('whe', validators=[Required()])
    len = FloatField('len', validators=[Required()])
    wid = FloatField('wid', validators=[Required()])
    hei = FloatField('hei', validators=[Required()])
    cur = FloatField('cur', validators=[Required()])
    engt = TextField('engt', validators=[Required()])
    noc = TextField('noc', validators=[Required()])
    engs = IntegerField('engs', validators=[Required()])
    fues = TextField('fues', validators=[Required()])
    bor = FloatField('bor', validators=[Required()])
    stro = FloatField('stro', validators=[Required()])
    com = FloatField('com', validators=[Required()])
    hor = IntegerField('hor', validators=[Required()])
    pea = IntegerField('pea', validators=[Required()])
    cit = IntegerField('cit', validators=[Required()])
    hig = IntegerField('hig', validators=[Required()])
    pri = FloatField('pri', validators=[Required()])
    
