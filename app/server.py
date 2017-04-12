from flask import render_template, flash, redirect, session,request, url_for, Response, g ,Flask
from flask_login import login_user, logout_user, current_user, login_required
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64
import os
import cognitive_face as CF

DATABASE_URI = 'sqlite:////tmp/github-flask.db'
SECRET_KEY = '7583782b420b4b189a43f243dad22119'
CF.Key.set(SECRET_KEY)

from random import Random
def random_str(randomlength=8):
    strs = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        strs+=chars[random.randint(0, length)]
    return strs
from forms import LoginForm, RegForm
app = Flask(__name__)
app.config.from_object(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
db.create_all()


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


def face_check(pic1,pic2):
    result1 = CF.face.detect(pic1)
    result2 = CF.face.detect(pic2)
    print(result1)
    print(result2)
    print(pic1)
    print(pic2)
    compare = CF.face.verify(face_id=result1[0]['faceId'],another_face_id=result2[0]['faceId'])
    print(compare['isIdentical'])
    return compare['isIdentical']
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    return render_template("index.html",
                           title="Home",
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.id.data, password=form.password.data).first():
            user = User.query.filter_by(username=form.id.data, password=form.password.data).first_or_404()
            login_user(user)
            print("logined")
            return redirect(url_for('index'))
        else:
            print("notlogined")
            return render_template('login.html',
                                   title='Sign In',
                                   error='Not Right',
                                   form=form)
    print("???")
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegForm()
    if form.validate_on_submit():
        f = form.filename.data
        filename = form.id.data+'.png'
        f.save(os.path.join(
            app.instance_path, filename
        ))
        filename = form.id.data+'.png'
        me = User(form.id.data,form.password.data,filename)
        db.session.add(me)
        db.session.commit()
        if User.query.filter_by(username=form.id.data, password=form.password.data).first():
            user = User.query.filter_by(username=form.id.data, password=form.password.data).first_or_404()
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html',
                                   title='Sign In',
                                   error='Not Right',
                                   form=form)
    return render_template('register.html',
                           title='Register',
                           form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/getimage')
@login_required
def getimage():
    image = open("./instance/"+g.user.username+'.png','rb').read()
    resp = Response(image,mimetype="image/jpeg")
    return resp

@app.route('/getrawimage/<username>')
def getrawimage(username):
    image = open("./instance/{}.png".format(username), 'rb').read()
    resp = Response(image, mimetype="image/jpeg")
    return resp

@app.route('/js/<javascript>')
def getjs(javascript):
    js = open("./js/{}".format(javascript), 'rb').read()
    resp = Response(js)
    return resp

@app.route('/getcam')
def getcam():
    return render_template('cam.html')

@app.route('/docamlogin', methods=['GET', 'POST'])
def docamlogin():
    c = request.form.get('doc')
    fs = open('temp.txt','w')
    fs.write(c)
    fs.close()
    fs = open('temp.txt','rb')
    tempfile = random_str(60)
    tempfilename = tempfile+'.png'
    f = open(os.path.join(
        app.instance_path, tempfilename
    ),'wb')
    base64.decode(fs,f)
    files = os.listdir(app.instance_path)
    for f in files:
        if (f != tempfilename):
            user1 = str(f).split('.')[0]
            imgurl2 = "http://ttbachyinsda.pub:810/getrawimage" + "/" + user1
            imgurl1 = "http://ttbachyinsda.pub:810/getrawimage/"+tempfile
            print(imgurl2,imgurl1)
            if (face_check(imgurl2, imgurl1)):
                user = User.query.filter_by(username=user1).first_or_404()
                login_user(user)
                return redirect(url_for('index'))
    return redirect(url_for('getcam'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    upload = db.Column(db.String(120))

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def __init__(self, username, password,filename):
        self.username = username
        self.password = password
        self.upload = filename

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8100,ssl_context='adhoc')
