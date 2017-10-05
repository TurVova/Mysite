from flask import render_template, flash, redirect, request, url_for
from .app import app, db
from .forms import RegistrationForm, LoginForm
import my_app.models

def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users(form.first_name.data, form.last_name.data, form.n_name.data,
                     form.password.data, form.email.data, form.age.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('show_entries'))
    return render_template('login.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         login_user(users)
#         flask.flash('Logged in successfully.')
#
#         next = flask.request.args.get('next')
#         if not is_safe_url(next):
#             return flask.abort(400)
#
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(somewhere)
