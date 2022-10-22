from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

'''
safe: convert tag to html --> looking at <strong>
capitalize: upper for the first letter
lower: lower letter for all letters
upper: upper letter for all letters
title: the first letter of every word = capitalized
trim: remove space from the end
striptags: strip tgas from hacker --> looking at <strong>
'''

#Create a route decorator
@app.route('/')
def index():
# 	return "<h1>Hello</h1>"
	first_name="Bam"
	stuff="this is <strong>Bold</strong> Text"
	fav_col=['blue', 'green', 'red']

	return render_template("index.html", 
		name=first_name,
		stuff=stuff,
		fav_col=fav_col)

#localhost:5000/user/Bam
@app.route('/user/<name>')
def user(name):
	# return "<h1>Hello {}</h1>".format(name)
	return render_template("user.html", _username=name)

#Create Custom Error Pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Tnternal Server URL
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500