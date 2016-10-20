from flask import Flask, render_template

app = Flask(__name__)
#app.config.from_object("config")
#app.config.from_pyfile('config.py')

from app.module_one.controllers import module_one

app.register_blueprint(module_one)