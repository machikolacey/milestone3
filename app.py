import os
from flask import (Flask, render_template, redirect,
                   request, url_for, flash, session, jsonify)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
from flask_paginate import Pagination, get_page_args
from datetime import datetime

if os.path.exists("env.py"):
    import env  # noqa: F401

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'brightonCafes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    return redirect("/memories/date/asc/no")
    

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "photo": "https://res.cloudinary.com/machikolacey/image/upload/" +
                     "v1607383655/milestone3/coffee_wdl8h8.jpg"
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        session['logged_in'] = True
        return redirect(url_for("your_account", username=session["user"]))
    return render_template("register.html")


@app.route('/get_cafes/<sort>/<order>')
def get_cafes(sort, order):

    if order == "asc":
        ord = 1
    else:
        ord = -1

    cafes = mongo.db.cafes.find().sort(sort, ord)

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)
    total = cafes.count()
    pagination_cafes = cafes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='bootstrap4')

    return render_template(
        "cafes.html", cafes=pagination_cafes, pagination=pagination)


@app.route('/add_cafe')
def add_cafe():
    if not session.get('logged_in'):
        return redirect("/login")
    areanames = mongo.db.areas.find()
    areanamesjson = dumps(areanames)

    return render_template('addcafe.html',
                           areas=mongo.db.areas.find(),
                           areanames=areanamesjson,
                           username=session["user"])


@app.route('/edit_cafe/<cafe_id>')
def edit_cafe(cafe_id):
    if not session.get('logged_in'):
        return redirect("/login")
    the_cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    all_areas = mongo.db.areas.find()
    return render_template('editcafe.html', cafe=the_cafe, areas=all_areas)


@app.route('/update_cafe/<cafe_id>', methods=['POST'])
def update_cafe(cafe_id):
    cafes = mongo.db.cafes
    cafes.update({'_id': ObjectId(cafe_id)},
                 {
        'cafe_name': request.form.get('cafe_name'),
        'website': request.form.get('website'),
        'address': request.form.get('address'),
        'postcode': request.form.get('postcode'),
        'area_name': request.form.get('area_name'),
        'photo': request.form.get('photo'),
        'youtube': request.form.get('youtube')
    })
    return redirect(url_for('get_cafes', sort='cafe_name', order='asc'))



@app.route('/insert_cafe', methods=["POST"])
def insert_cafe():

    area_id = mongo.db.areas.find_one(
        {"name": request.form.get('area_name')})["_id"]
    cafe = request.form.to_dict()
    cafe["area_id"] = area_id
    cafes = mongo.db.cafes
    cafes.insert_one(cafe)
    return redirect(url_for('get_cafes', sort='cafe_name', order='asc'))


@app.route('/insert_memory', methods=["POST"])
def insert_memory():

    memory = request.form.to_dict()

    date_object = datetime.strptime(memory["date"], '%d/%m/%Y')
    memory["date"] = date_object

    cafe_id = mongo.db.cafes.find_one(
        {"cafe_name": memory["cafe_name"]})["_id"]

    memory["cafe_id"] = cafe_id

    memories = mongo.db.memories
    memories.insert_one(memory)
    return redirect(url_for('get_memories', sort='date',
                            order='asc', is_yours='yes'))


@app.route('/add_memory')
def add_memory():
    if not session.get('logged_in'):
        return redirect("/login")
    cafes = mongo.db.cafes.find()
    cafenames = mongo.db.cafes.find({}, {"cafe_name": 1, "area": 1})
    user = mongo.db.users.find_one({"username": session.get("user")})

    cafenamesjson = dumps(cafenames)
    return render_template('addmemory.html',
                           cafes=cafes,
                           areas=mongo.db.areas.find(),
                           cafenames=cafenamesjson,
                           username=session.get('user'),
                           user=user)


@app.route('/filter_cafe', methods=['POST', 'GET'])
def filter_cafe():
    x = []
    cafes = mongo.db.cafes.find()

    for cafe in cafes:
        x.append(cafe)

        return jsonify(x)


@app.route('/memories/<sort>/<order>/<is_yours>')
def get_memories(sort, order, is_yours):

    if is_yours == 'yes':
        memories = mongo.db.memories.find({"user": session.get("user")})
    else:
        memories = mongo.db.memories.find()

    mems = []

    for memory in memories:

        user = mongo.db.users.find_one({"username": memory["user"]})

        try:
            memory["userphoto"] = user["photo"]
        except TypeError:
            memory["userphoto"] = "https://res.cloudinary.com/machikolacey/image/upload/v1607383655/milestone3/coffee_wdl8h8.jpg"

        cafe = mongo.db.cafes.find_one({'_id': ObjectId(memory["cafe_id"])})
        try:
            memory["area_name"] = cafe["area_name"]
        except TypeError:
            memory["area_name"] = ""

        memory["ukdate"] = memory["date"].strftime('%d/%m/%Y')
        mems.append(memory)

    if(order == "desc"):
        mems = sorted(mems, key=lambda x: x[sort], reverse=True)
    else:
        mems = sorted(mems, key=lambda x: x[sort], reverse=False)

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)
    total = len(mems)
    pagination_mems = mems[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='bootstrap4')

    if is_yours == 'yes':
        return render_template("yourmemories.html",
                               memories=pagination_mems, pagination=pagination)
    else:
        return render_template(
            "memories.html", memories=pagination_mems, pagination=pagination)


@app.route('/edit_memory/<memory_id>/<page>')
def edit_memory(memory_id, page):
    the_memory = mongo.db.memories.find_one({"_id": ObjectId(memory_id)})

    the_memory["ukdate"] = the_memory["date"].strftime('%d/%m/%Y')

    all_cafes = mongo.db.cafes.find()
    cafenames = mongo.db.cafes.find({}, {"cafe_name": 1, "area": 1})
    cafenamesjson = dumps(cafenames)

    return render_template('editmemory.html', memory=the_memory,
                           cafes=all_cafes, page=page, cafenames=cafenamesjson)


@app.route('/edit_account/<user_id>')
def edit_account(user_id):
    the_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('editaccount.html', user=the_user)


@app.route('/update_user/<user_id>', methods=["POST"])
def update_user(user_id):
    users = mongo.db.users
    users.update({'_id': ObjectId(user_id)},
                 {"$set": {
                     'username': request.form.get('username'),
                     'photo': request.form.get('photo')
                 }})
    return redirect(url_for('get_memories', sort='date',
                            order='asc', is_yours='yes'))


@app.route('/update_memory/<memory_id>/<page>', methods=["POST"])
def update_memory(memory_id, page=''):
    memories = mongo.db.memories

    date_object = datetime.strptime(request.form.get('date'), '%d/%m/%Y')

    memories.update({'_id': ObjectId(memory_id)},
                    {"$set": {
                        'cafe_name': request.form.get('cafe_name'),
                        'description': request.form.get('description'),
                        'photo': request.form.get('photo'),
                        'is_private': request.form.get('is_private'),
                        'date': date_object
                    }})
    if(page == "yourmemories"):
        return redirect(url_for('get_memories', sort='date',
                                order='asc', is_yours='yes'))
        return redirect(url_for('get_memories', sort='date',
                                order='asc', is_yours='no'))


@app.route('/delete_memory/<memory_id>/<page>')
def delete_memory(memory_id, page):
    mongo.db.memories.remove({'_id': ObjectId(memory_id)})
    if (page == 'yourmemories'):
        return redirect(url_for('get_memories', sort='date',
                                order='asc', is_yours='yes'))
    return redirect(url_for('get_memories', sort='date',
                            order='asc', is_yours='no'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")

                session['logged_in'] = True
                return redirect(
                    url_for('get_memories',
                            sort='date',
                            order='asc',
                            is_yours='yes'))

            else:
                # Invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # user doesn't exist
            flash("The user doesn't exist")
            return redirect(url_for("login"))
    return render_template("login.html")


def sort_memories(request):
    sort = request.GET._getitem_('sort')
    print(sort)
    return json.dumps(sort)


@app.route("/cafe/<cafe_id>", methods=["GET", "POST"])
def cafe(cafe_id):
    mems = []
    youtube = ""
    cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    memories = mongo.db.memories.find({"cafe_id": ObjectId(cafe_id)})
   
    try:
        if cafe['youtube']:
            youtube = cafe['youtube'].replace("watch?v=", "/embed/")
    except KeyError:
        print("The key does not exist!")

    for memory in memories:
        user = mongo.db.users.find_one({"username": memory["user"]})
        memory["userphoto"] = user["photo"]
        mems.append(memory)
    return render_template("cafe.html", cafe=cafe,
                           youtube=youtube, memories=mems)


@app.route('/logout')
def logout():
    session.pop("user")
    session.pop('logged_in', None)
    return redirect(url_for('get_memories', sort='date',
                            order='asc', is_yours='no'))


@app.route("/your_account/<username>", methods=["GET", "POST"])
def your_account(username):
    if session["user"]:
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("youraccount.html", user=user)

        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get("DEBUG_MODE"))
