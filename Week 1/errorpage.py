from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - Sanjna"

@app.route("/robots.txt")
def index():

	return render_template(
        'accessdenied.html'), 401


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)