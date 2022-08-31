from flask import Flask, render_template
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b'3fa3e40b00966748cdcc7024d410ae5d2e225438f724bf8f6f54b300598fe04d'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/question/<int:id>")
def show_question(id):
    return render_template('question.html', id=id)

@app.route("/profile/<int:id>")
def show_profile(id):
    return render_template('profile.html', id=id)
