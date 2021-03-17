import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

users_coll = mongo.db.users
stocks_coll = mongo.db.stocks
comments_coll = mongo.db.comments

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = users_coll.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "watched_stocks": []
        }

        users_coll.insert_one(signup)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # return redirect(url_for("watchlist", username=session["user"]))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = users_coll.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "watchlist", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/browse")
def browse():
    stocks = stocks_coll.find().sort("ticker_symbol")
    return render_template("browse.html", stocks=stocks)


@app.route("/get_stock/<stock_id>")
def get_stock(stock_id):
    stock = stocks_coll.find_one({"_id": ObjectId(stock_id)})
    return render_template("stock.html", stock=stock)


@app.route("/watchlist/<username>", methods=["GET", "POST"])
def watchlist(username):
    username = users_coll.find_one(
        {"username": session["user"]})
    # Create an empty array for watched stocks
    watched_stocks = []
    if session["user"]:
        # For each of the user's watched_stocks, finds the corresponding
        # id in the stocks collection and populates into temporary chain
        for stock in username["watched_stocks"]:
            watched_stocks_list = stocks_coll.find_one({
                "_id": ObjectId(stock)})
            watched_stocks.append(watched_stocks_list)
        return render_template("watchlist.html",
                                username=username,
                                watched_stocks=watched_stocks)
    # Else return back to login
    return redirect(url_for("login"))


@app.route("/remove_from_watchlist/<stock_id>")
def remove_from_watchlist(stock_id):
    username = users_coll.find_one(
        {"username": session["user"]})

    users_coll.find_one_and_update(
        {"username": session["user"]},
        {"$pull": {"watched_stocks": ObjectId(stock_id)}})
    return redirect(url_for("watchlist", username=username))


@app.route("/add_to_watchlist/<stock_id>")
def add_to_watchlist(stock_id):
    users_coll.find_one_and_update(
        {"username": session["user"]},
        {"$push": {"watched_stocks": ObjectId(stock_id)}})
    return redirect(url_for("browse"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # Make sure to set debug to false when moved to PROD
            debug=True)