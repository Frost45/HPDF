from flask import Flask, flash, redirect, render_template, request, session, abort, send_file
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - Sanjna"

@app.route("/html")
def index():

	return render_template(
        'randompage.html')

@app.route("/image")
def picture():

	images = [ 'Pictures\doge.jpg',
				'Pictures\Grumpy.jpg',
				'Pictures\ken.jpg',
				'Pictures\kylo.jpg',
				'Pictures\MissPiggy.jpg',
				'Pictures\nyancat.jpg',
				'Pictures\Pigeon.jpg']
	randomNumber = randint(0,6) 
	imagepath = images[randomNumber] 
 
	return send_file(imagepath,mimetype='image/gif')
		
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)