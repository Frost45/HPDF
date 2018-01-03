import json
import urllib.request
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - Sanjna"

@app.route("/authors")
def index():
	
	url1 = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users")
	authors = json.loads(url1.read().decode())
	url2 = urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts")
	posts = json.loads(url2.read().decode())

	authcount = []

	for person in authors:
		actemp = {}
		post_count = 0
		for post in posts:
			if post['userId'] == person['id']:
				post_count = post_count + 1
		actemp['name'] = person['name']
		actemp['post_count'] = post_count
		authcount.append(actemp)

	return render_template(
        'auth.html',author = authcount)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)