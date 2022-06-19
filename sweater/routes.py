import flask_login
from flask import render_template, redirect, request, flash, Blueprint
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from sweater.models import UserModel, db

app_route = Blueprint('app_route', __name__)


@app_route.route("/profile")
def profile_page():
    some = flask_login.current_user.username
    return render_template("profile.html", some=some)


@app_route.route("/register", methods=("POST", "GET"))
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['password'])
            user = UserModel(username=request.form['username'], email=request.form['email'], password=hash)
            db.session.add(user)
            db.session.flush()

            db.session.commit()

        except:
            db.session.rollback()
            print("error!!!")

    return render_template("register.html")


@app_route.route("/login", methods=("POST", "GET"))
def login_page():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user = UserModel.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect('/')
        else:
            flash('Check password, login')
    else:
        flash('fill login and password fields')

    return render_template('login.html')


@app_route.route('/logout', methods=("POST", 'GET'))
def logout():
    if request.method == 'GET':
        name = request.args.get('username')
        user = UserModel.query.filter_by(username=name).first()
        return user.logout_user()
