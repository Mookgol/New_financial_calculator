import random
import re
import sqlite3
import string
from datetime import datetime
import bcrypt
import math
import tkinter as tk
import tkinter as tk2
from tkinter import simpledialog, messagebox

# Welcome text
WELCOME_TEXT = """                         
                                                                              ,---------------------------,                                                         
                                                                              |  /---------------------\  |
                                                                              | |                       | |
                                                                              | |     we value          | |
                                                                              | |      customer         | |
                                                                              | |       time & needs    | |
                                                                              | |                       | |
                                                                              |  \_____________________/  |
                                                                              |___________________________|
                                                                            ,---\_____     []     _______/------,
                                                                          /         /______________\           /|                                                                           
                                                                        /___________________________________ /  | ___
                                                                        |                                   |   |    )
                                                                        |  _ _ _                 [-------]  |   |   (
                                                                        |  o o o                 [-------]  |  /    _)_
                                                                        |__________________________________ |/     /  /
                                                                    /-------------------------------------/|      ( )/
                                                                  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
                                                                /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
                                                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


888       888 8888888888 888       .d8888b.   .d88888b.  888b     d888 8888888888       88888888888  .d88888b.        888       .d88888b.   .d8888b.         d8888 888            888888b.          d8888 888b    888 888    d8P  
888   o   888 888        888      d88P  Y88b d88P" "Y88b 8888b   d8888 888                  888     d88P" "Y88b       888      d88P" "Y88b d88P  Y88b       d88888 888            888  "88b        d88888 8888b   888 888   d8P   
888  d8b  888 888        888      888    888 888     888 88888b.d88888 888                  888     888     888       888      888     888 888    888      d88P888 888            888  .88P       d88P888 88888b  888 888  d8P    
888 d888b 888 8888888    888      888        888     888 888Y88888P888 8888888              888     888     888       888      888     888 888            d88P 888 888            8888888K.      d88P 888 888Y88b 888 888d88K     
888d88888b888 888        888      888        888     888 888 Y888P 888 888                  888     888     888       888      888     888 888           d88P  888 888            888  "Y88b    d88P  888 888 Y88b888 8888888b    
88888P Y88888 888        888      888    888 888     888 888  Y8P  888 888                  888     888     888       888      888     888 888    888   d88P   888 888            888    888   d88P   888 888  Y88888 888  Y88b   
8888P   Y8888 888        888      Y88b  d88P Y88b. .d88P 888   "   888 888                  888     Y88b. .d88P       888      Y88b. .d88P Y88b  d88P  d8888888888 888            888   d88P  d8888888888 888   Y8888 888   Y88b  
888P     Y888 8888888888 88888888  "Y8888P"   "Y88888P"  888       888 8888888888           888      "Y88888P"        88888888  "Y88888P"   "Y8888P"  d88P     888 88888888       8888888P"  d88P     888 888    Y888 888    Y88b 



                    888888888         .d8888b.                           88888888888                                 d8888                          8888888b.                            .d8888b.                                   
                    888              d88P  Y88b       o                      888           o                        d88888       o                  888   Y88b       o                  d88P  Y88b       o                          
                    888              Y88b.           d8b                     888          d8b                      d88P888      d8b                 888    888      d8b                 Y88b.           d8b                         
                    8888888b.         "Y888b.       d888b                    888         d888b                    d88P 888     d888b                888   d88P     d888b                 "Y888b.       d888b                        
                         "Y88b           "Y88b. "Y888888888P"                888     "Y888888888P"               d88P  888 "Y888888888P"            8888888P"  "Y888888888P"                "Y88b. "Y888888888P"                    
                           888             "888   "Y88888P"                  888       "Y88888P"                d88P   888   "Y88888P"              888 T88b     "Y88888P"                    "888   "Y88888P"                      
                    Y88b  d88P       Y88b  d88P   d88P"Y88b                  888       d88P"Y88b               d8888888888   d88P"Y88b              888  T88b    d88P"Y88b              Y88b  d88P   d88P"Y88b                      
                     "Y8888P"         "Y8888P"   dP"     "Yb                 888      dP"     "Yb             d88P     888  dP"     "Yb             888   T88b  dP"     "Yb              "Y8888P"   dP"     "Yb          
  """
# Closing text
CLOSE_TEXT = """

 ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗ ██████╗ ██████╗     ██╗   ██╗███████╗██╗███╗   ██╗ ██████╗      ██████╗ ██╗   ██╗██████╗     ██████╗  █████╗ ███╗   ██╗██╗  ██╗ █████╗ ██████╗ ██████╗      ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗
  ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██╔═══██╗██╔══██╗    ██║   ██║██╔════╝██║████╗  ██║██╔════╝     ██╔═══██╗██║   ██║██╔══██╗    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║
     ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║    █████╗  ██║   ██║██████╔╝    ██║   ██║███████╗██║██╔██╗ ██║██║  ███╗    ██║   ██║██║   ██║██████╔╝    ██████╔╝███████║██╔██╗ ██║█████╔╝ ███████║██████╔╝██████╔╝    ██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║
     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║    ██╔══╝  ██║   ██║██╔══██╗    ██║   ██║╚════██║██║██║╚██╗██║██║   ██║    ██║   ██║██║   ██║██╔══██╗    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║██╔═══╝ ██╔═══╝     ██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
     ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝    ██║     ╚██████╔╝██║  ██║    ╚██████╔╝███████║██║██║ ╚████║╚██████╔╝    ╚██████╔╝╚██████╔╝██║  ██║    ██████╔╝██║  ██║██║ ╚████║██║  ██╗██║  ██║██║     ██║██╗      ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝       ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝

"""


# Function to create a database connection and cursor
class BankDatabase:
    def __init__(self, db_name='bankapp.db'):
        try:
            self.conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES)
            self.conn.row_factory = sqlite3.Row  # Set row_factory for named columns
            self.cursor = self.conn.cursor()
            self.create_tables()
            self.create_admin(self.cursor, self.conn)  # Create admin user on initialization
        except sqlite3.Error as e:
            print("Database connection error:", e)

    def create_tables(self):
        # Create necessary tables if they don't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, 
                              balance REAL, account_number TEXT UNIQUE)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, transaction_type TEXT, 
                              amount REAL, transaction_time DATETIME)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admins
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)''')
        self.conn.commit()

    def close_connection(self):
        # Close the database connection
        self.conn.close()

    def exit_program(self):
        # Close the database connection
        root.destroy()

    # Function to generate a random account number
    def generate_random_account_number(self):
        account_number = ''.join(random.choices(string.digits, k=10))
        return account_number

    # Function to create an admin user
    def create_admin(self, cursor, conn):
        cursor.execute("INSERT OR IGNORE INTO admins (username, password) VALUES (?, ?)",
                       ('admin', bcrypt.hashpw('admin@123'.encode('utf-8'), bcrypt.gensalt())))
        conn.commit()

    # Function to validate the password
    def is_valid_password(self, password):
        # Check if the password meets certain criteria (e.g., length, uppercase, lowercase, digits, special characters)
        # Return True if the password is valid, otherwise return False
        # Check if the password has at least 8 characters
        if len(password) < 8:
            return False

        # Check if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check if the password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check if the password contains at least one special character (e.g., !@#$%^&*)
        special_characters = r'[!@#$%^&*]'
        if not re.search(special_characters, password):
            return False

        return True
        # Function to handle user deposit

    # Update the user_deposit method
    def user_deposit(self, user, amount):
        if amount >= 10 and amount % 10 == 0 and amount > 0:
            # Calculate the new balance after deposit
            user_balance = user['balance'] + amount

            # Update user's balance in the database
            self.cursor.execute("UPDATE users SET balance=? WHERE account_number=?",
                                (user_balance, user['account_number']))

            # Get the current timestamp for the transaction
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Insert the deposit transaction into the transactions table
            self.cursor.execute(
                "INSERT INTO transactions (username, transaction_type, amount, transaction_time) VALUES (?, ?, ?, ?)",
                (user['username'], "Deposit", amount, transaction_time))
            self.conn.commit()

            # Log the deposit transaction
            self.log_transaction(user['username'], "Deposit", amount, user_balance)

            # Fetch the updated balance from the database
            self.cursor.execute("SELECT balance FROM users WHERE account_number=?", (user['account_number'],))
            updated_balance = self.cursor.fetchone()[0]

            # Print deposited amount and updated balance
            # print(f"Deposited: R{amount}")
            print(f"Current Balance: R{updated_balance}")  # Display updated balance after deposit
            return amount
        else:
            # Print error message for invalid deposit amount
            print("Invalid deposit amount. Please enter an amount above or equal to 10 and in multiples of 10.")
            return None

    # Update the user_withdraw method
    def user_withdraw(self, user, amount):
        if amount >= 60 and amount % 10 == 0:
            try:
                # Fetch the user's current balance from the database
                self.cursor.execute("SELECT balance FROM users WHERE username=?", (user['username'],))
                user_balance = self.cursor.fetchone()[0]

                # Check if the user has sufficient balance for the withdrawal
                if user_balance >= amount:
                    # Calculate the new balance after withdrawal
                    new_balance = user_balance - amount

                    # Update user's balance in the database
                    self.cursor.execute("UPDATE users SET balance=? WHERE username=?", (new_balance, user['username']))

                    # Get the current timestamp for the transaction
                    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Insert the withdrawal transaction into the transactions table
                    self.cursor.execute(
                        "INSERT INTO transactions (username, transaction_type, amount, transaction_time) VALUES (?, ?, ?, ?)",
                        (user['username'], "Withdrawal", amount, transaction_time))
                    self.conn.commit()

                    # Log the withdrawal transaction
                    self.log_transaction(user['username'], "Withdrawal", amount, new_balance)

                    # Fetch the updated balance from the database
                    self.cursor.execute("SELECT balance FROM users WHERE username=?", (user['username'],))
                    updated_balance = self.cursor.fetchone()[0]

                    # Print withdrawn amount and updated balance
                    # print(f"Withdrawn: R{amount}")
                    # print(f"Current Balance: R{updated_balance}")  # Display updated balance after withdrawal
                    return amount
                else:
                    # Print error message for insufficient balance
                    return "Insufficient balance for withdrawal."
            except sqlite3.Error as e:
                # Handle database error and print error message
                print("Database error:", e)
                return "An error occurred while processing the withdrawal. Please try again later."
        else:
            # Print error message for invalid withdrawal amount
            print("Invalid withdrawal amount. Please enter an amount above 50 and in multiples of 10.")
            return None

    # Function to log transactions in transaction_log.txt file
    def log_transaction(self, username, transaction_type, amount, transaction_time, balance):
        with open('transaction_log.txt', 'a') as file:
            log_entry = f"Username: {username}, Transaction Type: {transaction_type}, Amount: {amount}, Balance: {balance}, Time: {transaction_time}\n"
            file.write(log_entry)
        print("Transaction logged successfully.")

    # Function to validate initial deposit amount input
    def validate_initial_deposit(self, input_value):
        try:
            deposit_amount = float(input_value)
            if deposit_amount < 0:
                print("Initial deposit amount cannot be negative. Please enter a valid amount.")
                return None
            return deposit_amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the deposit amount.")
            return None

    # Function to create a new user account
    def create_account(self):
        while True:
            # username = input("Enter your username: ")
            username = simpledialog.askstring("Create Account", "Enter username:")
            if ' ' in username:
                print("Username cannot contain spaces. Please choose a different username.")
            else:
                self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
                existing_user = self.cursor.fetchone()
                if existing_user:
                    print("Username already in use. Please choose a different username.")
                else:
                    break

        while True:
            # password = input("Enter your password (at least 8 characters with special characters): ")
            password = simpledialog.askstring("Create Account", "Enter password:")
            if not self.is_valid_password(password):
                print(
                    "Invalid password. Please ensure your password has at least 8 characters with uppercase letters, lowercase letters, digits, and special characters.")
            else:
                break

        while True:
            # initial_deposit_input = input("Enter initial deposit amount: R")
            initial_deposit_input = simpledialog.askstring("Deposit", "Enter initial deposit amount: R")

            initial_deposit = self.validate_initial_deposit(initial_deposit_input)
            if initial_deposit is not None:
                break

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        account_number = self.generate_random_account_number()

        # Store user data in the users table
        self.cursor.execute("INSERT INTO users (username, password, balance, account_number) VALUES (?, ?, ?, ?)",
                            (username, hashed_password, initial_deposit, account_number))

        # Store user data in bankdata.txt
        with open('bankdata.txt', 'a') as bankdata_file:
            bankdata_file.write(f"Username: {username}, Account Number: {account_number}\n")

        # Log initial deposit transaction in the transactions table
        self.cursor.execute(
            "INSERT INTO transactions (username, transaction_type, amount, transaction_time) VALUES (?, ?, ?, ?)",
            (username, "Initial Deposit", initial_deposit, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.conn.commit()
        messagebox.showinfo("Popup Message", f"Account created successfully! Your account number is: {account_number}")
        # print(f"Account created successfully! Your account number is: {account_number}")

    # Function to handle user actions (deposit, withdrawal, etc.)
    def transact_screen(self):
        btn_deposit = tk2.Button(canvas, text="1. Deposit", command=bank_db.create_account)
        btn_deposit.pack(pady=10)

        btn_withdraw = tk2.Button(canvas, text="2. Withdraw", command=bank_db.logins)
        btn_withdraw.pack(pady=10)

        btn_view_balance = tk2.Button(root, text="3. View Balance", command=bank_db.remove_user)
        btn_view_balance.pack(pady=10)

        btn_view_transaction_history = tk2.Button(root, text="4. View Transaction History", command=bank_db.exit_program)
        btn_view_transaction_history.pack(pady=10)

        btn_calculator = tk2.Button(root, text="5. Calculator", command=bank_db.exit_program)
        btn_calculator.pack(pady=10)

        btn_logout = tk2.Button(root, text="6. Logout", command=bank_db.exit_program)
        btn_logout.pack(pady=10)

    def handle_user_actions(self, user_data):
        # Display the user's current balance when they log in
        print(f"Current Balance: R{user_data['balance']}")

        # Start an infinite loop to handle user actions
        while True:
            # Display the menu options
            root_2 = tk2.Tk()
            root_2.title("Transact")
            canvas_2 = tk2.Canvas(root_2)
            canvas_2.pack()
            self.transact_screen()
            # print("\n1. Deposit")
            # print("2. Withdraw")
            # print("3. View Balance")  # Option to view balance
            # print("4. View Transaction History")
            # print("5. Calculator")
            # print("6. Logout")

            # Get the user's choice
            choice = input("Enter your choice: ")

            # Perform actions based on user's choice
            if choice == "1":
                # Handle deposit functionality
                deposit_amount = float(input("Enter deposit amount: R"))
                if deposit_amount > 0:
                    deposited_amount = self.user_deposit(user_data, deposit_amount)
                    if deposited_amount is not None:
                        user_row = self.cursor.execute("SELECT * FROM users WHERE username=?",
                                                       (user_data['username'],)).fetchone()
                        user_data = dict(user_row)
                        print(f"Deposited: R{deposited_amount}")
                        print(f"Current Balance: R{user_data['balance']}")  # Display updated balance after deposit
                else:
                    print("Invalid deposit amount. Please enter a positive value.")
            elif choice == "2":
                # Handle withdrawal functionality
                withdrawal_amount = float(input("Enter withdrawal amount: R"))
                if withdrawal_amount > 0:
                    withdrawn_amount = self.user_withdraw(user_data, withdrawal_amount)
                    if isinstance(withdrawn_amount, float):
                        user_row = self.cursor.execute("SELECT * FROM users WHERE username=?",
                                                       (user_data['username'],)).fetchone()
                        user_data = dict(user_row)
                        print(f"Withdrawn: R{withdrawn_amount}")
                        print(f"Current Balance: R{user_data['balance']}")  # Display updated balance after withdrawal
                    else:
                        print(withdrawn_amount)  # Display error message if withdrawal fails
                else:
                    print("Invalid withdrawal amount. Please enter a positive value.")
            elif choice == "3":
                # Display current balance when the user selects this option
                print(f"Current Balance: R{user_data['balance']}")
            elif choice == "4":
                # Handle viewing transaction history
                self.cursor.execute("SELECT * FROM transactions WHERE username=?", (user_data[1],))
                transactions = self.cursor.fetchall()
                print("\nTransaction History:")
                for transaction in transactions:
                    print(f"Type: {transaction[2]}, Amount: R{transaction[3]}, Time: {transaction[4]}")
            elif choice == "5":
                self.financial_calculator()
            elif choice == "6":
                # Logout the user and exit the loop
                print("Logout successful.")
                break
            else:
                # Handle invalid choices
                print("Invalid choice! Please try again.")

    # Function to log transactions to transaction_log.txt
    def log_transaction(self, username, transaction_type, amount, balance):
        with open('transaction_log.txt', 'a') as file:
            log_entry = f"Username: {username}, Transaction Type: {transaction_type}, Amount: {amount}, Balance: {balance}, Time: {datetime.now()}\n"
            file.write(log_entry)
        print("Transaction logged successfully.")

    # Function to handle admin actions
    def handle_admin_actions(self):
        # admin_username = input("Enter admin username: ")
        # admin_password = input("Enter admin password: ")
        admin_username = simpledialog.askstring("", "Enter admin username: ")
        admin_password = simpledialog.askstring("", "Enter admin password: ")

        # Authenticate admin
        self.cursor.execute("SELECT * FROM admins WHERE username=?", (admin_username,))
        admin_data = self.cursor.fetchone()

        if admin_data and bcrypt.checkpw(admin_password.encode('utf-8'), admin_data[2].encode('utf-8')):
            print("Admin login successful!")
            while True:
                print("\n1. Remove User")
                print("2. View All Users")
                print("3. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    # account_number = input("Enter account number to remove user: ")
                    account_number = simpledialog.askstring("Remove User", "Enter username to remove:")
                    self.remove_user(account_number)
                elif admin_choice == "2":
                    self.cursor.execute("SELECT * FROM users")
                    users = self.cursor.fetchall()
                    print("\nAll Users:")
                    for user in users:
                        print(f"Username: {user[1]}, Account Number: {user[4]}, Balance: R{user[3]}")
                elif admin_choice == "3":
                    print("Admin logout successful.")
                    break
                else:
                    print("Invalid choice! Please try again.")
        else:
            print("Invalid admin credentials. Access denied.")

    # Function to remove user
    def remove_user(self, account_number):
        self.cursor.execute("SELECT * FROM users WHERE account_number=?", (account_number,))
        user_data = self.cursor.fetchone()

        if user_data:
            self.cursor.execute("DELETE FROM users WHERE account_number=?", (account_number,))
            self.cursor.execute("DELETE FROM transactions WHERE username=?", (user_data[1],))
            self.conn.commit()
            print(f"User with account number {account_number} has been removed successfully.")
        else:
            print("Invalid account number. Please try again.")

    # Function to handle user login
    def login(self):
        while True:
            # username = input("Enter your username: ")
            username = simpledialog.askstring("Login", "Enter username:")
            # password = input("Enter your password: ")
            password = simpledialog.askstring("Login", "Enter password:")

            self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            user_data = self.cursor.fetchone()

            if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[2].encode('utf-8')):
                print("Login successful!")
                return user_data
            else:
                print("Invalid username or password. Please try again.")
                continue

    def financial_calculator(self):
        while True:
            print("Welcome to the Financial Calculator!")
            print("Choose a calculation: ")
            print("1.Investment")
            print("2. Bond ")
            user_choice = input("Enter your choice: ").strip().lower()

            if user_choice == '1':
                principal = float(input("Enter Investment amount: "))
                while principal < 0:
                    print("Please enter a valid amount.")
                    principal = float(input("Enter Investment amount: "))

                interest_rate = float(input("Enter the interest rate (as a decimal): "))
                while interest_rate < 0:
                    print("Please enter a valid rate.")
                    interest_rate = float(input("Enter the interest rate (as a decimal): "))

                years = int(input("Enter the number of years you plan on investing for: "))
                while years < 0:
                    print("Please enter a valid number of years.")
                    years = int(input("Enter the number of years you plan on investing for: "))

                interest_type = input(
                    "Enter 1 for: 'simple' interest or Enter 2 for: 'compound' interest? ").strip().lower()
                if interest_type == '1':
                    # Calculate simple interest for investment
                    interest_amount = principal * (1 + interest_rate * years)
                    print(f"Your total amount after {years} years with simple interest will be: {interest_amount:.2f}")
                elif interest_type == '2':
                    # Calculate compound interest for investment
                    compound_interest = principal * math.pow((1 + interest_rate), years)
                    print(
                        f"Your total amount after {years} years with compound interest will be: {compound_interest:.2f}")
                else:
                    print("Invalid interest type. Please enter 'simple' or 'compound'.")

            elif user_choice == '2':
                present_value = float(input("Enter the present value of the house: "))
                while present_value < 0:
                    print("Please enter a valid amount.")
                    present_value = float(input("Enter the present value of the house: "))

                annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
                while annual_interest_rate < 0:
                    print("Please enter a valid rate.")
                    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))

                years = int(input("Enter the number of years over which the bond will be repaid: "))
                while years < 0:
                    print("Please enter a valid number.")
                    years = int(input("Enter the number of years over which the bond will be repaid: "))

                monthly_interest_rate = (annual_interest_rate / 100) / 12
                total_payments = years * 12
                # Calculate monthly repayment using the provided formula
                repayment = (monthly_interest_rate * present_value) / (
                        1 - (1 + monthly_interest_rate) ** -total_payments)
                print(f"You will have to repay approximately {repayment:.2f} each month for the bond.")

            else:
                print("Invalid choice. Please enter 'Investment' or 'Bond'.")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if another_calculation != 'yes':
                print("Thank you for using the Financial Calculator. Goodbye!")
                break

    # Main function to drive the program

    def logins(self):
        user_data = bank_db.login()
        if user_data:
            print("works")
            self.clear_canvas()
            bank_db.handle_user_actions(user_data)

    def clear_canvas(self):
        # Delete all widgets on the canvas
        for widget in canvas.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    # Main function to drive the program
    root = tk.Tk()
    root.title("Financial Banking App")
    canvas = tk.Canvas(root)
    canvas.pack()

    bank_db = BankDatabase()
    # while True:
    #     try:
    btn_create_account = tk.Button(canvas, text="1. Create Account", command=bank_db.create_account)
    btn_create_account.pack(pady=10)

    btn_login = tk.Button(canvas, text="2. Login", command=bank_db.logins)
    btn_login.pack(pady=10)

    btn_remove_user = tk.Button(root, text="3. Admin - Remove User", command=bank_db.remove_user)
    btn_remove_user.pack(pady=10)

    btn_exit = tk.Button(root, text="4. Exit", command=bank_db.exit_program)
    btn_exit.pack(pady=10)
    # bank_db.clear_canvas()
            # print("1. Create Account")
            # print("2. Login")
            # print("3. Admin - Remove User")
            # print("4. Exit")
            # choice = input("Enter your choice: ")
            # choice = simpledialog.askstring("","Enter your choice")

        #
        # except Exception as e:
        #     print("An unexpected error occurred:", e)

    root.mainloop()
