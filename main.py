from flask import Flask, render_template, request, jsonify
from IntsaMain import InstaBot
from time import sleep

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/following", methods=["POST"])
def receive_data():
    username = request.form.get("username")
    password = request.form.get("password")
    targetid = request.form.get("targetid")
    ob = InstaBot()
    ob.login(username=username, password=password)
    ob.find_followers(targetid=targetid)
    ob.startFollowing()
    sleep(2)
    ob.quitServer()
    return "<h1>Done</h1>"
 

if __name__ == "__main__":
    app.run(debug=True)
