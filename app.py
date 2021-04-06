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
    """ This renders the index page """
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
                    # flash("Welcome, {}".format(request.form.get("username")))
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
    """ This clears the session """
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("index"))


@app.route("/home/<username>")
def home(username):
    """ This gets stocks for browse page """
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        latest_comments = list(comments_coll.find().sort("_id", -1).limit(20))
        # comments = []
        # for comment in latest_comments:
        #     matching_stock = stocks_coll.find_one({"comments": ObjectId(comment["_id"])})
        #     comments.append(matching_stock)
        return render_template("home.html",
                                latest_comments=latest_comments)
    else:
        return redirect(url_for("index"))

@app.route("/browse/<filter>")
def browse(filter):
    """ This gets stocks for browse page """
    countries = ['USA', 'UK']
    stock_markets = ['NASDAQ', 'NYSE', 'LSE']
    # If filter is all, find all stocks
    if filter == "ALL":
        stocks = stocks_coll.find().sort("ticker_symbol")
    # Otherwise filter according to dropdown selection
    elif filter in countries:
        stocks = stocks_coll.find({"country": filter}).sort("ticker_symbol")
    elif filter in stock_markets:
        stocks = stocks_coll.find({"market_name": filter}).sort("ticker_symbol")
    # If user logged in, identify their watched stocks
    if 'user' in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_stocks = username["watched_stocks"]
        return render_template("browse.html", 
                                stocks=stocks, 
                                watched_stocks=watched_stocks,
                                filter=filter)
    return render_template("browse.html",
                            stocks=stocks,
                            filter=filter)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ This gets the search query from the search form """
    query = request.form.get("search")
    return redirect(url_for('results', query=query))


@app.route("/results/<query>", methods=["GET", "POST"])
def results(query):
    """ This searches for the query in the stocks collection """
    query = query
    stocks = list(stocks_coll.find({"$text": {"$search": query}}))
    # If logged in user, identify their watched stocks
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        watched_stocks = username["watched_stocks"]
        return render_template("results.html", 
                                query=query, 
                                watched_stocks=watched_stocks,
                                stocks=stocks)
    return render_template("results.html", query=query, stocks=stocks)


@app.route("/get_stock/<stock_id>")
def get_stock(stock_id):
    """ This gets the stock with the stock id """
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
    # Loops over the stock's comment Object Ids
    for comment in stock["comments"]:
        # Finds the corresponding comments in the comments collection
        stock_comments = comments_coll.find_one({"_id": ObjectId(comment)})
        # Pushes those comments into the empty comments array
        comments.append(stock_comments)
    # Finds number of comments
    commentsNo = len(comments)
    # If user logged in, indentify if stock is in their watchlist
    if "user" in session:
        result = users_coll.find_one({"username": session["user"],
                "watched_stocks": ObjectId(stock_id)})
        if result is None:
            watched_stock = False
        else:
            watched_stock = True
    # If not logged in, watched stock set to False
    else:
        watched_stock = False
    return render_template("stock.html", stock=stock
                                        , stock_price=stock_price
                                        , percentage_change=percentage_change
                                        , price_change=price_change
                                        , comments=comments
                                        , comments_no=commentsNo
                                        , watched_stock=watched_stock)


@app.route("/add_comment/<stock_id>", methods=["POST"])
def add_comment(stock_id):
    """ This adds a new comment to the stock """
    if "user" in session:
        # Gets the date and time comment created
        created_on = datetime.today().strftime('%d/%m/%Y, %H:%M:%S')
        new_comment = {
            "username": session["user"],
            "date_created": created_on,
            "comment": request.form.get("stock-comment")
        }
        # Adds comment to comments collection
        insert_comment = comments_coll.insert_one(new_comment)
        # Adds comment id to the stock's comments array
        stocks_coll.update_one({"_id": ObjectId(stock_id)},
                                {"$push": {"comments":
                                {"$each": [insert_comment.inserted_id],
                                "$position": 0}}})
        flash("Your comment was succesfully added")
        return redirect(url_for("get_stock",
                            stock_id=stock_id))
    else:
        return redirect(url_for("get_stock",
                            stock_id=stock_id))


@app.route("/edit_comment/<stock_id>/<comment_id>", methods=["POST"])
def edit_comment(stock_id, comment_id):
    """ This edits a user's comment """
    if "user" in session:
        # Get the edited comment
        edited_comment = request.form.get("edited-comment")
        # Update the comment in the comments collection
        comments_coll.update_one({"_id": ObjectId(comment_id)},
                                {"$set": {"comment": edited_comment}})
        flash("Your comment was succesfully edited")
        return redirect(url_for("get_stock",
                            stock_id=stock_id))
    else:
        return redirect(url_for("get_stock",
                            stock_id=stock_id))


@app.route("/delete_comment/<stock_id>/<comment_id>")
def delete_comment(stock_id, comment_id):
    """ This deletes a user's comment """
    if "user" in session:
        # Remove the comment from the comments collection
        comments_coll.remove({"_id": ObjectId(comment_id)})
        # Remove the comments ObjectId from the stock's comments array
        stocks_coll.update_one({"_id": ObjectId(stock_id)},
                                {"$pull": {"comments": ObjectId(comment_id)}})
        flash("Your comment was succesfully deleted")
        return redirect(url_for("get_stock",
                            stock_id=stock_id))
    else:
        return redirect(url_for("get_stock",
                            stock_id=stock_id))


@app.route("/watchlist/<username>", methods=["GET", "POST"])
def watchlist(username):
    """ This gets the user's watchlist """
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        # Create an empty array for watched stocks
        watched_stocks = []
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
    else:
        return redirect(url_for("index"))


@app.route("/remove_from_watchlist/<stock_id>/<url>/<filter>/<query>")
def remove_from_watchlist(stock_id, url, filter, query):
    """ This removes a stock from the user's watchlist """
    if "user" in session:
        username = users_coll.find_one(
            {"username": session["user"]})
        # Remove the stock id from the user's watched_stocks 
        users_coll.find_one_and_update(
            {"username": session["user"]},
            {"$pull": {"watched_stocks": ObjectId(stock_id)}})
        # If this was removed from browse page, redirect back to there
        if url == "browse":
            return redirect(url_for("browse", filter=filter))
        if url == "search":
            return redirect(url_for("results", query=query))
        # Otherwise redirect to the user's watchlist
        else:
            return redirect(url_for("watchlist", username=username))
    else:
        return redirect(url_for("index"))


@app.route("/add_to_watchlist/<stock_id>/<url>/<filter>/<query>")
def add_to_watchlist(stock_id, url, filter, query):
    """ This adds a stock to the user's watchlist """
    if "user" in session:
        # Add the stock id to the user's watched stocks
        users_coll.find_one_and_update(
            {"username": session["user"]},
            {"$push": {"watched_stocks": ObjectId(stock_id)}})
        # If this was added from browse page, redirect back to there
        if url == "browse":
            return redirect(url_for("browse", filter=filter))
        # If this was added from search page, redirect back to there
        if url == "search":
            return redirect(url_for("results", query=query))
        else:
            return redirect(url_for("get_stock",
                                stock_id=stock_id))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # Make sure to set debug to false when moved to PROD
            debug=True)