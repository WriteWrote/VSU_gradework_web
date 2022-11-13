from flask import Blueprint, render_template
main = Blueprint("main", __name__)


@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')
    # return "main page here"


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/result")
def result():
    return render_template('result.html', title='Result')
