from flask import Flask, request, render_template,url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["hr_mananagement"]
collection = db["employees"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup",methods = ["POST"])
def signup():
       if request.method == "POST":
              username = request.form["username"]
              password = request.form["password"]
              dic = {}
              dic[username] = password
              collection.insert_one(dic)
              return "Credentials Inserted"
       
@app.route("/database",methods = ["GET"])
def database():
       if request.method == "GET":
              col = list(collection.find({},{"_id":0}))              
              return col

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        doc = collection.find_one({username: password}, {"_id": 0})
        if doc:
            return "Logged In Successfully!!"
        else:
            return "Incorrect credentials"

    return render_template("login.html")




@app.route("/register")
def register():
       return render_template("register.html")


if __name__ == "__main__":
	 app.run(host = "127.0.0.6",port=6060,debug=True)