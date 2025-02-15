from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/boost')
def boost():
    return render_template('boost.html')

@main.route('/friends')
def friends():
    return render_template('friends.html')

@main.route('/tasks')
def tasks():
    return render_template('tasks.html')

@main.route('/wallet')
def wallet():
    return render_template('wallet.html')