from flask import Flask, render_template,request
import flask
from pymongo import MongoClient
import datetime


app = Flask(__name__)
client = MongoClient("mongodb+srv://jc4529:jc4529@dbms.7l8pp.mongodb.net/?retryWrites=true&w=majority")
app.db = client.cyberdb


@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        fname = request.form.get("fname")
        email = request.form.get("email")
        complain = request.form.get("complain")
        formatted_date=datetime.datetime.today().strftime("%m-%d-%Y")
        app.db.cyberrep.insert_one({"fname":fname,"email":email,"complain":complain, "date":formatted_date})
    

    return render_template('index.html')


@app.route("/admin", methods=["GET"])
def admin():
    entries_with_date = [
        (  entry["fname"],
            entry["email"], 
            entry["complain"], 
            # entry["date"],
            # datetime.datetime.strptime(entry["date"], "%m-%d-%Y").strftime("%b %d")
        )
        for entry in app.db.cyberrep.find({})
    ]
    return render_template('admin.html',entries=entries_with_date)



app.run(debug=True)  
