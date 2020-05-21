from flask import Flask

app =Flask(__name__)

@app.route("/")
def  home():
    return "Hello,world !!"

@app.route("/<string:name>")
def  name_function(name):
      return  f"Hello, {name}!"
