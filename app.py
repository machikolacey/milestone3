import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'brightonCafes'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster.1nsni.mongodb.net/brightonCafes?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_cafes')
def get_cafes():
    return render_template("cafes.html", cafes=mongo.db.cafes.find())

@app.route("/register", methods=["GET", "POST"])
def register():
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