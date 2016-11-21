from flask import Blueprint, request, render_template

module_one = Blueprint("auth", __name__, url_prefix="/auth")


@module_one.route("/hello")
def hello():
	return "My nam is Dang Van Dai, this is my app!!!"
