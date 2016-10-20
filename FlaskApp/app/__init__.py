from flask import Flask, render_template

app = Flask(__name__)

from app.module_one.controllers import module_one

app.register_blueprint(module_one)

@app.route("/")
def home():
	return "This is app only show what is my name? </br> My name is Dang Van Dai"