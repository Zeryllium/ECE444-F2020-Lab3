from datetime import datetime
from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_moment import Moment
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Email


app = Flask(__name__, template_folder='html-templates-activity2')
app.config['SECRET_KEY'] = 'secret stringy string'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    uoft_email = "utoronto"

    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your email?', validators=[DataRequired(), Email(), ])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name and old_name != form.name.data:
            flash('You have changed your name!')
        if old_email and old_email != form.email.data:
            flash('You have changed your email!')

        session['name'] = form.name.data
        session['email'] = form.email.data

        return redirect(url_for('index'))

    return render_template('index.html', current_time=datetime.utcnow(), form=form,
                           name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')