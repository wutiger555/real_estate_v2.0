from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)


@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('dashboard.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)