import os
from flask import Flask, render_template, redirect, request, url_for, flash, session, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 
from bson import json_util
import json
from bson.json_util import dumps
app = Flask(__name__)



app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["MONGO_DBNAME"] = 'brightonCafes'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster.1nsni.mongodb.net/brightonCafes?retryWrites=true&w=majority"

mongo = PyMongo(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 



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
        session['logged_in'] = True
        return redirect(url_for("profile", username = session["user"] ))
    return render_template("register.html")



@app.route('/get_cafes')
def get_cafes():
    return render_template('cafes.html',
         cafes=mongo.db.cafes.find())

@app.route('/add_cafe')
def add_cafe():
    if  session.get('logged_in') != True:
       return redirect("/login")   
    areanames=mongo.db.areas.find()
    areanamesjson = dumps(areanames)
    
    return render_template('addcafe.html',
           areas=mongo.db.areas.find(), areanames=areanamesjson,  username = session["user"])



@app.route('/edit_cafe/<cafe_id>')
def edit_cafe(cafe_id):
    if  session.get('logged_in') != True:
      return redirect("/login")   
    the_cafe =  mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    all_areas =  mongo.db.areas.find()
    return render_template('editcafe.html', cafe=the_cafe, areas=all_areas)






@app.route('/update_cafe/<cafe_id>', methods=['POST'])
def update_cafe(cafe_id):
    cafes = mongo.db.cafes
    cafes.update( {'_id':ObjectId(cafe_id)},
    {
        'cafe_name':request.form.get('cafe_name'),
        'website':request.form.get('website'),
        'address': request.form.get('address'),
        'area_name': request.form.get('area_name')
        
    })
    return redirect(url_for('get_cafes'))

@app.route('/delete_cafe/<cafe_id>')
def delete_cafe(cafe_id):
    mongo.db.cafes.remove({'_id': ObjectId(cafe_id)})
    return redirect(url_for('get_cafes'))




@app.route('/insert_cafe', methods=["POST"])
def insert_cafe():

    area_id = mongo.db.areas.find_one({"name":request.form.get('area_name')})["_id"]
    cafe = request.form.to_dict()
    cafe["area_id"] = area_id
   
    cafes = mongo.db.cafes
    cafes.insert_one(cafe)
    return redirect(url_for("get_cafes"))






@app.route('/insert_memory', methods=["POST"])
def insert_memory():
 
    memory = request.form.to_dict()

    print(memory["cafe_name"])
    cafe_id = mongo.db.cafes.find_one({"cafe_name":memory["cafe_name"]})["_id"]
    
    memory["cafe_id"] = cafe_id
    memory["user_id"] = ObjectId(request.form.get("user_id"))
    memories = mongo.db.memories
    memories.insert_one(memory)
    return redirect(url_for("get_memories"))


@app.route('/add_memory')
def add_memory():
    if  session.get('logged_in') != True:
      return redirect("/login")   
    cafes=mongo.db.cafes.find()
    cafenames=mongo.db.cafes.find({}, {"cafe_name":1, "area":1})
    user = mongo.db.users.find_one({"username":session.get("user")})

    cafenamesjson = dumps(cafenames)
    return render_template('addmemory.html',
           cafes=cafes, areas=mongo.db.areas.find(), cafenames= cafenamesjson, username = session.get('user'), user=user )

@app.route('/filter_cafe',  methods=['POST', 'GET'])
def filter_cafe():
    x   = []
    cafes=mongo.db.cafes.find()
  
    for cafe in cafes:
     x.append(cafe)

     return jsonify(x)

@app.route('/')
def get_memories():
    memories=mongo.db.memories.find()
    users=mongo.db.users.find()
    mems = []
   
    for memory in memories:

            user = mongo.db.users.find_one({"username":memory["user"]})            
            memory["userphoto"] = user["photo"]
            mems.append(memory)
    return render_template("memories.html", memories=mems)
    

@app.route('/your_memories')
def your_memories():
    if  session.get('logged_in') != True:
      return redirect("/login")   
    return render_template("yourmemories.html", memories=mongo.db.memories.find(), 
                                  username = session.get('user') )


@app.route('/cafe_autocomplete/<query>')
def cafe_autocomplete():
    cafes = cafes=mongo.db.memories.find()
    print(cafes)
    return  cafes




@app.route('/edit_memory/<memory_id>/<page>')
def edit_memory(memory_id, page):
    the_memory =  mongo.db.memories.find_one({"_id": ObjectId(memory_id)})
    all_cafes =  mongo.db.cafes.find()
    cafenames=mongo.db.cafes.find({}, {"cafe_name":1, "area":1})
    cafenamesjson = dumps(cafenames)
    return render_template('editmemory.html', memory=the_memory,
                           cafes=all_cafes, page = page, cafenames=cafenamesjson)


@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    the_user =  mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('edituser.html', user=the_user)

@app.route('/update_user/<user_id>', methods=["POST"])
def update_user(user_id):
    users = mongo.db.users
    users.update( {'_id': ObjectId(user_id)},
    {"$set": {
        'username':request.form.get('username'),
        'photo':request.form.get('photo')
    }})
    return redirect(url_for('profile', username=session['user']))

@app.route('/update_memory/<memory_id>/<page>', methods=["POST"])
def update_memory(memory_id, page=''):
    memories = mongo.db.memories
    memories.update( {'_id': ObjectId(memory_id)},
    {"$set": {
        'cafe_name':request.form.get('cafe_name'),
        'description':request.form.get('description'),
        'photo':request.form.get('photo'),
        'is_private': request.form.get('is_private'),
        'date': request.form.get('date')
    }})
    if(page == "yourmemories"):
           return redirect(url_for('your_memories'))
    return redirect(url_for('get_memories'))


@app.route('/delete_memory/<memory_id>/<page>')
def delete_memory(memory_id, page):
    mongo.db.memories.remove({'_id': ObjectId(memory_id)})
    if (page == 'yourmemories'):
          return redirect(url_for('your_memories'))
    return redirect(url_for('get_memories'))





@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        existing_user = mongo.db.users.find_one(
            {"username":request.form.get("username").lower()})
        if existing_user:
            #ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"]    = request.form.get("username")
              
                flash("welcome, {}".format(request.form.get("username")))
                session['logged_in'] = True
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
            #Invalid password match
                flash("Incorrect username annd/or password")
                return redirect(url_for("login"))   
        else:
            #user doesn't exist
            flash("The user doesn't exist")
            return redirect (url_for("login"))
    return render_template("login.html")           

@app.route('/logout')
def logout():
    flash('You have been logged out')
    session.pop("user")
    session.pop('logged_in', None)
    return redirect(url_for("login"))

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
      user = mongo.db.users.find_one({"username" : session["user"]})
      if session["user"]:
         return render_template("profile.html", user=user)
    
         return redirect(url_for('login'))


def cafe_autocomplete(request, **kwargs):
    term = request.GET.__getitem__('query')
    cafes = [str(cafe) for cafe in    cafe.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))] 
    return  HttpResponse(json.dumps(cafes))   


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)