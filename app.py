from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/about/")
def about():
    return "This is about page."


@app.route("/main")
def main():
    return "This is main page."


@app.route("/hello")
@app.route("/hello/<name>")
def say_hi(name="guest"):
    return render_template('hello.html', name=name)


@app.route("/id/<int:id>")
def show_id(id):
    return f"id = {id + 1}"


if __name__ == "__main__":
    app.run()
