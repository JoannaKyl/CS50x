import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    cash = db.execute("SELECT cash from users WHERE id = ?", user_id)
    user_cash = cash[0]["cash"]
    # trading = db.execute("SELECT symbol, SUM(shares) as shares, SUM(total) as total from (SELECT symbol, shares, shares * price as total FROM trades WHERE user_id = ?) as t GROUP BY symbol;", user_id)
    monies = db.execute("SELECT symbol ,sum(trades.shares) as shares ,users.cash-(sum(trades.shares*trades.price) )as cash_on_hand , sum(trades.shares*trades.price) as stock_value, trades.price from trades JOIN users on users.id = trades.User_id and trades.user_id = ? group by trades.symbol;", user_id)
    portfolios = db.execute("SELECT sum(trades.shares*trades.price) as stock_value, (users.cash-(sum(trades.shares*trades.price) )+sum(trades.shares*trades.price)) as total_asset,users.cash-(sum(trades.shares*trades.price) )as cash_on_hand from trades  JOIN users on users.id = trades.User_id and trades.user_id = ?  group by trades.user_id;", user_id)
    return render_template("index.html",  user_cash=user_cash, monies=monies, portfolios=portfolios)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT symbol,shares,price ,timestamp FROM trades WHERE user_id =?;", user_id)
    return render_template("history.html", transactions=transactions)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():

    if request.method == "GET":
        return render_template("deposit.html")

    if request.method == "POST":
        deposit = request.form.get("deposit")

        if int(deposit) < 1:
            return apology("Deposit must greater than 1")

        user_id = session["user_id"]
        cash = db.execute("SELECT cash from users Where id =?", user_id)
        original_cash = cash[0]["cash"]
        current_balance = float(original_cash) + float(deposit)

        try:
            db.execute("Update users SET cash =? Where id =?", current_balance, user_id)
        except ValueError:
            return apology("Unable to update")

        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)

        if not symbol:
            return apology("Missing Symbol")

        if not quote:
            return apology("Invalid Symbol")

    return render_template("/quoted.html", symbol=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Username is required")

        if not password:
            return apology("Password is required")

        if not confirmation:
            return apology("Confirmation is required")

        if confirmation != password:
            return apology("Confirmation does not match password")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")))
        except ValueError:
            return apology("Username already exists")

        return redirect("/")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Missing Symbol")

        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid Symbol")

        shares = request.form.get("shares")
        try:
            shares = int(shares)
            if (shares < 1):
                raise ValueError("")
        except ValueError:
            return apology("Shares must be an integer and greater than 1")

        price = (quote)["price"]
        total = int(shares) * int(price)
        user_id = session["user_id"]
        cash = db.execute("SELECT cash from users WHERE id = ?", user_id)
        user_cash = cash[0]["cash"]

        if total > user_cash:
            return apology("Cannot afford")

        try:
            db.execute("INSERT INTO trades (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                       user_id, symbol, shares, quote["price"])
            # delete update users.cash
        except ValueError:
            return apology("Unable to add")

    flash("Bought!")
    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols = db.execute("SELECT distinct(symbol) from trades WHERE user_id = ? ", user_id)
        return render_template("/sell.html", symbols=symbols)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol == None:
            return apology("Missing Symbol")

        shares = request.form.get("shares")
        user_id = session["user_id"]
        dbshares = db.execute(
            "SELECT sum(trades.shares) as shares from trades WHERE symbol =? and user_id =? Group by symbol;", symbol, user_id)
        user_shares = dbshares[0]['shares']
        if int(shares) > int(user_shares):
            return apology("Too many shares")

        if int(shares) < int(1):
            return apology("Shares must be greater than 1")

        quote = lookup(symbol)
        price = quote['price']
        cash = db.execute("SELECT cash from users Where id =?", user_id)
        original_cash = cash[0]["cash"]
        cash_gain = float(price) * float(shares)

        try:
            db.execute("Update users SET cash =? Where id =?", original_cash+cash_gain, user_id)
        except ValueError:
            return apology("Unable to update")

        try:
            db.execute("INSERT INTO trades (user_id ,symbol ,shares ,price ) VALUES(?, ?, ?, ?)",
                       session["user_id"], symbol, (-1) * shares, price)
        except ValueError:
            return apology("Unable to update")

    flash("Sold!")
    return redirect("/")
