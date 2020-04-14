from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/hi/<name>")
def say_hi(name):
    return f"Hi~ {name}"

if __name__ == "__main__":
    app.run()