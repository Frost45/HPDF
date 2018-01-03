from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - Sanjna"

@app.route("/input", methods=["GET", "POST"])
def index():
	
	if request.method == "POST":
		username = request.form['username']
		return redirect('/hello/'+username)
	
	return render_template('form.html')

@app.route('/hello/<username>')
def users(username):
	
	return "Hello " + username
	

	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)