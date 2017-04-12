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
    sym = IntegerField('sym')
    nor = IntegerField('nor')
    mak = TextField('mak')
    fue = TextField('fue')
    asp = TextField('asp')
    nod = TextField('nod')
    bod = TextField('bod')
    dri = TextField('dri')
    eng = TextField('eng')
    whe = FloatField('whe')
    len = FloatField('len')
    wid = FloatField('wid')
    hei = FloatField('hei')
    cur = FloatField('cur')
    engt = TextField('engt')
    noc = TextField('noc')
    engs = IntegerField('engs')
    fues = TextField('fues')
    bor = FloatField('bor')
    stro = FloatField('stro')
    com = FloatField('com')
    hor = IntegerField('hor')
    pea = IntegerField('pea')
    cit = IntegerField('cit')
    hig = IntegerField('hig')
    pri = FloatField('pri')
    
