from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def home():
    return render_template('login.html')

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

@app.route('/login_submit', methods=['POST'])
def login_submit():
    if request.method == 'POST':
        role = request.values['username']
        if role == 'buyer':
            return render_template('dashboard.html')
        else:
            return render_template('dashboard_gov.html')
        return render_template('login.html')

@app.route('/index_gov')
def index_gov():
    return render_template('dashboard_gov.html')

@app.route('/user_gov')
def user_gov():
    return render_template('user_gov.html')
    

if __name__ == '__main__':
    app.run(debug=True)