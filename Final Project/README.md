# CoinStock

CoinStock is a web application that allows individuals to quote the prices of cryptocurrencies and stocks, as well as to record their portfolios, including stocks, cryptocurrencies, income, and savings.

## Demo

Please visit: [Demo Video](https://youtu.be/EXDXoUhw4uk)

## Description

1. **Main Functions:**
   1. **Register & Login Functions:**
        1. **Register:**
            * Before accessing the functions of the website, all users must register with CoinStock.
                - The email will be used as the username, and each email is allowed to register only one account.
                - The email and hashed password will be inserted into the users table.
        2. **Login:**
            * On the login page, users are required to input their email and password.
                - The system will check whether the email matches the data in the database.
                - The function `check_password_hash()` will be used to verify whether the inputted password matches the hashed password.
                - Login is required to access the **Income**, **Saving**, **Quote**, **Stock**, **Crypto**, and **Portfolio** functions.

   2. **Record Monthly Savings and Income:**
        * After logging into their accounts, users can input their savings and income details, which will be inserted into the database based on `session["user_id"]`.

   3. **Quote Current Prices of Stocks & Cryptocurrencies:**
        * The libraries `yahoo-finance` and `cryptocompare` need to be installed for this function. The functions `stock_quote` and `crypto_quote` are defined in `investment_data.py`, which is imported in `app.py`.
            ```bash
            pip install yfinance
            ```
            ```bash
            pip install cryptocompare
            ```

   4. **Track Portfolio:**
        * Based on `session["user_id"]`, users' savings, coins, and stock data will be displayed in `portfolio.html`.

   5. **Logout:**
        * The logout function will be implemented using `session.clear()`.

   6. **Dark Mode:**
        * JavaScript is used to change the background color and font color when the `dark_mode_theme` button is clicked. This sets the dark mode on, and `localStorage` will be used to remember the dark mode preference.

2. **Database: CoinStock.db**
     - To meet the different needs of CoinStock, there are five tables in the `coinstock.db` file:
        1. **User:**
            ```sql
            users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, email TEXT NOT NULL, hash TEXT NOT NULL);
            ```

        2. **Saving:**
            ```sql
            saving (id INTEGER PRIMARY KEY AUTOINCREMENT, month INTEGER NOT NULL, saving INTEGER NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
            ```
            - `user_id` is a FOREIGN KEY from the `id` of the users table.

        3. **Income:**
            ```sql
            income (id INTEGER PRIMARY KEY AUTOINCREMENT, month INTEGER NOT NULL, income INTEGER NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
            ```
            - `user_id` is a FOREIGN KEY from the `id` of the users table.

        4. **Coin:**
            ```sql
            coin (id INTEGER PRIMARY KEY AUTOINCREMENT, Coin_symbol TEXT NOT NULL, quantities INTEGER NOT NULL, price INTEGER NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, user_id INTEGER NOT NULL, amount INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
            ```
            - `user_id` is a FOREIGN KEY from the `id` of the users table.

        5. **Stock:**
            ```sql
            stock (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL, shares INTEGER NOT NULL, price INTEGER NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, user_id INTEGER NOT NULL, amount INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
            ```
            - `user_id` is a FOREIGN KEY from the `id` of the users table.
