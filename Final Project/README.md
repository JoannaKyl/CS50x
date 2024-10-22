# CoinStock

CoinStock is a web page application for individuals quote the price of crypto and stock and to record their portfolio including stock,crypto,income and saving.

## Demo

Please visit: https://youtu.be/EXDXoUhw4uk


## Description

1. Main Function:
   1. Register & Login function
        1. Register
            * Before access the function of the website,all user must be registered with coinstock.
                - Email will be used as user name and each email only allow to register one account.
                - Email and hased password will insert into users table.
        2. Login
            * In the login page user are required to input their email and user name.
                - The system will check whether the email match the data in the database
                - ```check_password_hash()``` will be adopted to check whether inputted password is the same with hashed password (hash)
                -Login is required for access for ```Income``` ,```Saving``` , ```Quote``` , ```Stock```, ```Crypto``` and ```Portfolio```

   2. Allow users to record monthly saving and income
        * After login the account , inputted saving and income details will be inserted in the database based on the ```session["user_id"]```

   3. Allow users to qoute current price of stock & cryptocurrency

        * Libraries of yahoo-finance and cryptocompare need to be installed for this function.
          The function of  ```stock_quote``` and ```crypto_quote``` are in ```investment_data.py```
          ,which was imported in ```app.py```
            ```
            pip install yfinance

            ```
            ```
            pip install cryptocompare
            ```


   4. Allow users to track their portfolio
        *Based on ```session[user_id]``` ,user's ``` saving``` ,``` coin``` and ``` stock``` data will be displayed in ``` portfolio.html```

   5. Logout
        * Logout function will be implement by ``` session.clear()```

    6. Dark Mode
        *Using Javascript to change the background color and font color when the ```dark_mode_them``` button is clicked which set the dark mode on , and ```localStorage``` will be saved for the dark mode

2. Database:Coinstock.db
     - In order to different needs of the Coinstock,there are 5 tables in ```coinstock.db``` file:
        1. User

            ```
            users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, email TEXT NOT NULL, hash TEXT NOT NULL);
            ```

        2. Saving
            ```
            saving ( id INTEGER PRIMARY KEY AUTOINCREMENT, month INTEGER NOT NULL, saving INTEGER NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id) );
            ```
             - user_id is a FOREIGN KEY from ```id``` of users table

        3. Income
            ```
            income( id INTEGER PRIMARY KEY AUTOINCREMENT, month INTERGER NOT NULL, income INTERGER NOT NULL, user_id INTERGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id) );
            ```
            - user_id is a FOREIGN KEY from ```id``` of users table
            -

        4. Coin
             ```
            coin( id INTEGER PRIMARY KEY AUTOINCREMENT, Coin_symbol TEXT NOT NULL, quantities INTERGER NOT NULL, price INTERGER NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, user_id INTERGER NOT NULL, amount INTERGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id) );
            ```
            -  user_id is a FOREIGN KEY from ```id``` of users table

        5. Stock
            ```
            stock( id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL, shares INTERGER NOT NULL, price INTERGER NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, user_id INTERGER NOT NULL, amount INTERGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id) );
            ```
             - user_id is a FOREIGN KEY from ```id ``` of users table



