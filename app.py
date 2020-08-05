import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["MONGO_DBNAME"] = 'brightonCafes'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster.1nsni.mongodb.net/brightonCafes?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_cafes')
def get_cafes():
    return render_template("cafes.html", cafes=mongo.db.cafes.find())

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        #check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username":request.form.get("username").lower()}
        )
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username" : request.form.get("username").lower(),
            "password" : generate_password_hash(request.form.get("password"))            
        }    
 
        mongo.db.users.insert_one(register)

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
    return render_template("register.html")

@app.route('/insert_cafe', methods=["POST"])
def insert_cafe():
    cafes = mongo.db.cafes
    cafes.insert_one(request.form.to_dict())
    return redirect(url_for("get_cafes"))


@app.route('/add_cafe')
def add_cafe():
    return render_template('addcafe.html',
           areas=mongo.db.areas.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)