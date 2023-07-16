from flask import Blueprint, render_template, redirect, url_for, flash
from Users import routes as userRoutes
from Course import routes as courseRoutes
import json
main = Blueprint('main', __name__)

# Your Code Here
@main.route('/')
def index():
    return render_template('base.html')

@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/login', methods=['GET', 'POST'])
def login_post():
    response = userRoutes.login()
    if(response is None):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.login'))
    else:
        return redirect(url_for('main.courses'))

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup_post():
    response = userRoutes.signup()
    print(response)
    if(response is None):
        flash('User Already Exists.')
        return redirect(url_for('main.signup'))
    else:
        return redirect(url_for('main.login'))

@main.route('/logout')
def logout():
    userRoutes.logout()
    return redirect(url_for('main.index'))

@main.route('/courses')
def courses():
    courses = courseRoutes.courses()
    data = json.loads(courses.data.decode('utf-8'))
    return render_template('courses.html', course=data['courses'])