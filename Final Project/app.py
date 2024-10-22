import os
from flask import Flask, redirect, render_template, request, session, flash, make_response
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from investment_data import stock_quote, crypto_quote
from functools import wraps

db = SQL("sqlite:///coinstock.db")

app = Flask(__name__)
app.secret_key = 'thesecretley'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") == None:
            flash("Login Required.")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')


@app.route('/register', methods=["POST" ,"GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password-confirmation")

        if not email:
            flash("Email is required!")
            return redirect("/register")

        if password_confirmation != password:
            flash("Password confirmation must be the same as password")
            return redirect("/register")

        user = db.execute("SELECT email FROM users WHERE email = ?", request.form.get("email"))
        if user == email :
             flash("User already exist!")
             return redirect("/register")

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            db.execute("Insert into users (email ,hash) VALUES(?, ?)",email,hashed_password)
        except ValueError:
            flash("Account invalid!")
            return redirect("/register")

        flash("Account Created!")
        return redirect("/login")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.execute("SELECT email FROM users WHERE email = ?", request.form.get("email"))
        existing_user = user[0]["email"]
        if email != existing_user :
             flash("User not found.")
             return redirect("/login")

        user_id = db.execute("SELECT id FROM users WHERE email = ?", request.form.get("email"))
        check_password = db.execute("SELECT hash FROM users WHERE email = ?", request.form.get("email"))
        database_password = check_password[0]["hash"]
        if check_password_hash(database_password,password):
            session["user_id"] = user_id[0]["id"]
        else:
             flash("Incorrect Email or Password.")
             return redirect("/login")

    flash("Welcome Back!")
    return render_template("/index.html")



@app.route("/saving", methods=["POST","GET"])
@login_required
def saving():
    if request.method == "GET":
        return render_template('saving.html')

    if request.method == "POST":
        month = request.form.get("month")
        monthly_saving = request.form.get("saving")
        user_id = session["user_id"]
        print(f"{user_id }")
        if int(month) < 1 or int(month) > 12 :
            flash("Month must between 1-12")
            return redirect("/saving")

        if int(monthly_saving) < 0 :
            flash("Saving cannot be negative number.")
            return redirect("/saving")

        try:
            db.execute("Insert into saving (user_id,saving,month) VALUES(?, ?, ?)",user_id ,monthly_saving,month)
        except ValueError:
            flash("Unable to save.")
            return redirect("/saving")

    flash("Record added!")
    return redirect("/saving")

@app.route("/income", methods=["POST","GET"])
@login_required
def income():
        if request.method == "GET":
            return render_template('income.html')

        if request.method == "POST":
            month = request.form.get("month")
            monthly_income = request.form.get("income")
            user_id = session["user_id"]

        if int(month) < 1 or int(month) > 12 :
            flash("Month must between 1-12")
            return redirect("/income")

        if int(monthly_income) < 0 :
            flash("Income cannot be negative number.")
            return redirect("/income")

        try:
            db.execute("Insert into income (user_id,income,month) VALUES(?, ?, ?)",user_id ,monthly_income,month)
        except ValueError:
            flash("Unable to save.")
            return redirect("/income")

        flash("Record added!")
        return redirect("/income")

@app.route("/stock", methods=["POST","GET"])
@login_required
def stock():
        if request.method == "GET":
            return render_template('stock.html')

        if request.method == "POST":
            symbol = request.form.get("symbol")
            amount = request.form.get("amount")
            shares = request.form.get("shares")
            market_price = stock_quote (symbol)
            user_id = session["user_id"]

        if not symbol:
            flash("Symbol Required")
            return redirect("/stock")

        if int(shares) < 1 :
            flash("Shares must be equal or greater than 1")
            return redirect("/stock")

        if float(amount) < 0 :
            flash("Amount must be a postitive number")
            return redirect("/amount")

        try:
            db.execute("Insert into stock (user_id, symbol, amount, shares, price) VALUES(?, ?, ?, ?, ?)",user_id, symbol, amount, shares, market_price)
        except ValueError:
            flash("Incorrect Symbol.")
            return redirect("/stock")

        flash("Saved")
        return redirect("/stock")

@app.route("/crypto", methods=["POST","GET"])
@login_required
def coin():
        if request.method == "GET":
            return render_template('crypto.html')

        if request.method == "POST":
            coin = request.form.get("coin")
            qunatity = request.form.get("qunatity")
            amount = request.form.get("amount")
            user_id = session["user_id"]
            market_price = crypto_quote(coin)

        if not coin :
            flash("Coin Symbol Required")
            return redirect("/crypto")

        if int(qunatity) < 1 :
            flash("Shares must be equal or greater than 1")
            return redirect("/crypto")

        if float(amount) < 0 :
            flash("Amount must be a postitive number")
            return redirect("/crypto")

        try:
            db.execute("Insert into coin (user_id, Coin_symbol , quantities, amount, price) VALUES(?, ?, ?, ?, ?)",user_id, coin, qunatity, amount, market_price)
        except ValueError:
            flash("Incorrect Symbol.")
            return redirect("/crypto")

        flash("Saved")
        return redirect("/crypto")

@app.route("/portfolio")
@login_required
def portfolio():
        user_id = session["user_id"]
        income = db.execute("SELECT month ,SUM(income) as total_income from income WHERE user_id =? Group by month", user_id)
        saving = db.execute("SELECT month ,SUM(saving) as total_saving from saving WHERE user_id =? Group by month", user_id)
        stock = db.execute("SELECT symbol,SUM(shares) as total_shares ,SUM(amount) as total_amount from stock WHERE user_id =? Group by symbol", user_id)
        coin = db.execute("SELECT Coin_symbol, SUM(quantities) as total_quantities , SUM(amount) as total_amount from coin WHERE user_id =? Group by Coin_symbol", user_id)
        return render_template('portfolio.html',incomes =income, savings = saving, stocks = stock, coins = coin)

@app.route("/quote", methods=["POST","GET"])
@login_required
def quote():
    if request.method == "GET":
        return render_template('quote.html')

    if request.method == "POST":
        symbol = request.form.get("symbol")
        asset_type = request.form.get("asset")

    stock_price = stock_quote (symbol)
    crypto_price = crypto_quote (symbol)
    if asset_type == "Stock" and stock_price is None or asset_type == "Crypto" and crypto_price is None :
        flash("Symbol not found!")
        return redirect("/quote")

    if asset_type == "Stock":
        stock_price = stock_quote (symbol)
        flash(f"The current price of {symbol} is ${stock_price} USD")
        return redirect("/quote")

    if asset_type == "Crypto":
        crypto_price = crypto_quote(symbol)
        flash(f"The current price of {symbol} is ${crypto_price} USD")
        return redirect("/quote")

    if  asset_type != "Stock" or asset_type != "Crypto":
        flash("Please choose the asset type")
        return redirect("/quote")

@app.route("/logout", methods=["POST","GET"])
def logout():
    session.clear()
    flash("You are sucessfully logged out.")
    return render_template("/index.html")


