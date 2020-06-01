from flask import Flask, render_template

app  =  Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/more")
def more():
    return render_template("more.html")
