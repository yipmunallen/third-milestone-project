import os
import yfinance as yf
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/browse")
def browse():
    stocks = stocks_coll.find().sort("ticker_symbol")
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_stocks = username["watched_stocks"]
        return render_template("browse.html", 
                                stocks=stocks, 
                                watched_stocks=watched_stocks)
    return render_template("browse.html", stocks=stocks)    


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    stocks = list(stocks_coll.find({"$text": {"$search": query}}))
    return render_template("browse.html", stocks=stocks)


@app.route("/get_stock/<stock_id>")
def get_stock(stock_id):
    stock = stocks_coll.find_one({"_id": ObjectId(stock_id)})
    # Get current stock price from yfinance api
    # https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance
    ticker = yf.Ticker(stock["ticker_symbol"])
    todays_data = ticker.history(period='1d')
    stock_price_raw = todays_data['Close'][0]
    stock_price = round(stock_price_raw, 2)
    # Get yesterday's stock price at close from yfinance api
    yesterday_data = ticker.history(period='2d')
    yesterday_data_raw = yesterday_data['Close'][0]
    # Calculate change in price and percentage change
    # between yesterday close and today
    percentage_change_raw = 100*(stock_price_raw - yesterday_data_raw)/yesterday_data_raw
    percentage_change = round(percentage_change_raw, 2)
    price_change_raw = stock_price_raw - yesterday_data_raw
    price_change = round(price_change_raw, 2)
    # Create empty comments array and set number of comments to 0
    comments = []
    commentsNo = 0
    # Loops over the ObjectId's in the story_chains array in the story document
    for comment in stock["comments"]:
        stock_comments = comments_coll.find_one({"_id": ObjectId(comment)})
        # pushes those chain id's into the empty list)
        comments.append(stock_comments)
        commentsNo += 1
    if session["user"]:
        result = users_coll.find_one({"username": session["user"],
                "watched_stocks": ObjectId(stock_id)})
        if result == None:
            watched_stock = False
        else:
            watched_stock = True
    return render_template("stock.html", stock=stock
                                        , stock_price=stock_price
                                        , percentage_change=percentage_change
                                        , price_change=price_change
                                        , comments=comments
                                        , comments_no=commentsNo
                                        , watched_stock=watched_stock)


@app.route("/add_comment/<stock_id>", methods=["POST"])
def add_comment(stock_id):
    created_on = datetime.today().strftime('%d/%m/%Y, %H:%M:%S')
    new_comment = {
        "username": session["user"],
        "date_created": created_on,
        "comment": request.form.get("stock-comment")
    }
    insert_comment = comments_coll.insert_one(new_comment)
    stocks_coll.update_one({"_id": ObjectId(stock_id)},
                            {"$push": {"comments":
                            {"$each": [insert_comment.inserted_id],
                            "$position": 0}}})
    return redirect(url_for("get_stock",
                        stock_id=stock_id))


@app.route("/edit_comment/<stock_id>/<comment_id>", methods=["POST"])
def edit_comment(stock_id, comment_id):
    edited_comment = request.form.get("edited-comment")
    comments_coll.update_one({"_id": ObjectId(comment_id)},
                            {"$set": {"comment": edited_comment}})
    return redirect(url_for("get_stock",
                        stock_id=stock_id))


@app.route("/delete_comment/<stock_id>/<comment_id>")
def delete_comment(stock_id, comment_id):
    comments_coll.remove({"_id": ObjectId(comment_id)})
    stocks_coll.update_one({"_id": ObjectId(stock_id)},
                            {"$pull": {"comments": ObjectId(comment_id)}})
    return redirect(url_for("get_stock",
                        stock_id=stock_id))


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
        # https://therenegadecoder.com/code/how-to-sort-a-list-of-dictionaries-in-python/
        watched_stocks.sort(key=lambda item: item.get("ticker_symbol"))
        return render_template("watchlist.html",
                                username=username,
                                watched_stocks=watched_stocks)
    # Else return back to login
    return redirect(url_for("login"))


@app.route("/remove_from_watchlist/<stock_id>/<url>")
def remove_from_watchlist(stock_id, url):
    username = users_coll.find_one(
        {"username": session["user"]})

    users_coll.find_one_and_update(
        {"username": session["user"]},
        {"$pull": {"watched_stocks": ObjectId(stock_id)}})
    if url == "browse":
        return redirect(url_for("browse"))
    elif url == "stock":
        return redirect(url_for("get_stock",
                            stock_id=stock_id))
    else:
        return redirect(url_for("watchlist", username=username))


@app.route("/add_to_watchlist/<stock_id>/<url>")
def add_to_watchlist(stock_id, url):
    users_coll.find_one_and_update(
        {"username": session["user"]},
        {"$push": {"watched_stocks": ObjectId(stock_id)}})
    if url == "browse":
        return redirect(url_for("browse"))
    else:
        return redirect(url_for("get_stock",
                            stock_id=stock_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # Make sure to set debug to false when moved to PROD
            debug=True)