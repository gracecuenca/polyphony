from flask import Flask, session, url_for, redirect, render_template, request
import urllib2
import requests
import json


#App instantiation
app = Flask(__name__)
#app.secret_key = os.urandom(32)



@app.route("/")
def homepage():
    return redirect("/questions") 

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/results")
def results():
    sentence = request.args['sentence']
    print sentence
    return render_template("results.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
