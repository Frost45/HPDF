from flask import Flask, flash, redirect, render_template, request, session, abort, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - Sanjna"

@app.route("/setcookie")
def setcook():
	resp = make_response(redirect('/'))
	resp.set_cookie('name', value = "Sanjna", max_age = 90)
	resp.set_cookie('age', value = "21", max_age = 90)
	return resp

@app.route("/getcookie")
def getcook():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return "Name: " + name + " " + "Age: " + age


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)