from flask import render_template
from flask import Flask
app = Flask(__name__)
@app.route("/data_to")
def data_to():
some_pars = {'user':'Ivan','color':'red'}
some_str = 'Hello my dear friends!'
some_value = 10
return render_template('simple.html',some_str = some_str,
some_value = some_value,some_pars=some_pars)
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeI2PcaAAAAAFFrENF59lFzOhzD1OIP9EIZ0kNl'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeI2PcaAAAAAAuCgoZ4PHcy59UJyZSD22eEafEI'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
class NetForm(FlaskForm):
openid = StringField('openid', validators = [DataRequired()])
upload = FileField('Load image', validators=[
FileRequired(),
FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
recaptcha = RecaptchaField()
submit = SubmitField('send')
from werkzeug.utils import secure_filename
import os
import net as neuronet
@app.route("/net",methods=['GET', 'POST'])
def net():
form = NetForm()
filename=None
cfile = base64.b64decode(filebytes)
img = Image.open(BytesIO(cfile))
decode = neuronet.getresult([img])
neurodic = {}
for elem in decode:
neurodic[elem[0][1]] = str(elem[0][2])
print(elem)
ret = json.dumps(neurodic)
resp = Response(response=ret,
status=200,
mimetype="application/json")
return resp

