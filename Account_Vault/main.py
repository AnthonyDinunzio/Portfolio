# Project description: GUI Accounts Vault

# Import libraries
import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk

# Store already displayed accounts here so they are not duplicated
shown_accounts = []

# Store the password variable to a string till it is assigned
password = str

# Initialize the main window of the application as root
root = Tk()

# Using sqlite3 create a master database to hold the master password
conn = sqlite3.connect('master.db')

# Set the db cursor to a variable cursor
cursor = conn.cursor()

# Create a table in the master db if it does not already exist
cursor.execute("""CREATE TABLE IF NOT EXISTS masterpassword(
                            password TEXT NOT NULL
                          )""")


# Using sqlite3 create an accounts database to store accounts saved by user
accts = sqlite3.connect('accounts.db')

# Set the db cursor to a variable
accts_cursor = accts.cursor()

# Create a table to store usernames and passwords as an account if table does not already exist
accts_cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
                username text,
                password text
                )""")

# Save the tables
conn.commit()
accts.commit()


# Define a function to hold the information and logic for the vault screen
def vaultScreen():
    # Clear all previous text/buttons/etc
    for widget in root.winfo_children():
        widget.destroy()

    # Initialize the accounts db to keep track of all its enteries
    sql = "SELECT * FROM accounts"
    accts_cursor.execute(sql)
    rows = accts_cursor.fetchall()
    total = accts_cursor.rowcount
    print("Total Data Enteries: " + str(total))


    # Initialize the window for the vault screen
    root.geometry("600x600")
    root.title("Account Vault")

    # Draw the elements on the vault screen
    title = Label(root, text="Account Vault", font=200)
    title.config(anchor=CENTER)
    title.pack()

    frame = Frame(root)
    frame.pack()

    tv = ttk.Treeview(frame, columns=(1, 2),show="headings", height=10)
    tv.pack()

    tv.heading(1, text="Username")
    tv.heading(2, text="Password")


    # Define an updateView function to update the window with all the stored accounts in the database whenever a button is clicked
    def updateView():
        # Find any accounts in the accounts table in the accounts db
        accts_cursor.execute("SELECT * FROM accounts")
        # If there are any accounts
        if accts_cursor.fetchall():
            # For item in row
            for i in rows:
                # If item already in shown_accounts skip this item
                if i in shown_accounts:
                    pass
                # Else draw the items values to the table on the vault screen
                else:
                    tv.insert('', 'end', values=i)
                    tv.pack()
                    shown_accounts.append(i)
        # Other wise there are not accounts saved yet ie no table created
        else:
            print("No accounts saved")

    view_btn = Button(root, text="View", padx=30, pady=10, command=updateView)
    view_btn.place(x=400, y=550)


    # Define a function to add a new account to save to the database when a button is clicked
    def addAccount():
        # Create a new tkinter window for the account add tab
        acct_tab = Tk()
        # Configure the account tab window
        acct_tab.geometry("300x150")
        acct_tab.title("Add Account")

        # Draw all the elements on the add account tab
        heading = Label(acct_tab, text="Enter Username")
        heading.config(anchor=CENTER)
        heading.pack()

        username_ent = Entry(acct_tab, width=20)
        username_ent.pack()

        heading1 = Label(acct_tab, text="Enter Password")
        heading1.pack()

        password_ent = Entry(acct_tab, width=20)
        password_ent.pack()


        # Define a saveAccount function to automatically store the account typed by the user when the button is clicked
        def saveAccount():
            # Get username entered
            username = username_ent.get()
            # Get password entered
            password = password_ent.get()
            # Insert the username and the password into the accounts table
            accts_cursor.execute("INSERT INTO accounts VALUES(:username, :password)", {'username': username, 'password': password})
            acct_tab.destroy()
            accts.commit()


        save_acct_btn = Button(acct_tab, text="Save account", padx=15, pady=5, command=saveAccount)
        save_acct_btn.pack()



    add_btn = Button(root, text="Add Account", padx=20, pady=10, command=addAccount)
    add_btn.place(x=100, y=550)


# Define a login screen for the user to enter the master password for access to the account vault
def loginScreen():
    # Clear everything from the screen
    for widget in root.winfo_children():
        widget.destroy()
    # Reinitialize the window
    root.geometry("300x150")
    root.title("Account Vault | Login")

    # Draw all the elements of the loginScreen to the screen
    title = Label(root, text="WELCOME BACK", font=80)
    title.config(anchor=CENTER)
    title.pack()

    heading = Label(root, text="Enter Master Password")
    heading.config(anchor=CENTER)
    heading.pack()

    master_pwd_attempt = Entry(root, width=20, show="*")
    master_pwd_attempt.pack()


    # Define a function to find and retrive the password held inside master.db
    def getMasterPassword():
        # Set the password to a variable
        check_hashed_password = master_pwd_attempt.get()
        # Find if the variable entered matches the password in the database
        cursor.execute("SELECT * FROM masterpassword WHERE password = ?", [(check_hashed_password)])
        # Return any instances where the passwords matched
        return cursor.fetchall()

    # Define a function to take the entered password and the hashed password and compare them
    def checkPassword():
        match = getMasterPassword()

        # If the checkPassword function finds a match from the getMasterPassword function bring user to vaultScreen
        if match:
            vaultScreen()
        # Otherwise the password entered was incorrect
        else:
            heading2 = Label(root, text="Incorrect Password")
            heading2.pack()

    submit = Button(root, text="Submit", padx=15, pady=5, command=checkPassword)
    submit.config(anchor=CENTER)
    submit.pack()


# Define a screen for the very first time a user opens this application
def firstScreen():
    # Initialize screen
    root.geometry("300x150")
    root.title("Account Vault | Signup")

    # Draw elements for firstScreen to screen
    title = Label(root, text="WELCOME NEW USER", font=80)
    title.config(anchor=CENTER)
    title.pack()

    heading = Label(root, text="Create Master Password")
    heading.config(anchor=CENTER)
    heading.pack()

    mastpwd_ent = Entry(root, show="*", width=20)
    mastpwd_ent.pack()

    heading1 = Label(root, text="Re-enter Password")
    heading1.pack()

    reenter_ent = Entry(root, show="*", width=20)
    reenter_ent.pack()

    # Define a function that checks if both the passwords the user entered matches
    def checkPasswords():
        # If passwords are equal to each other insert password into master db then redirect to vaultScreen
        if mastpwd_ent.get() == reenter_ent.get():
            hashed_password = mastpwd_ent.get()
            insert_password = """INSERT INTO masterpassword(password) VALUES(?)"""
            cursor.execute(insert_password, [(hashed_password)])
            conn.commit()
            print("Saved Successfully")
            vaultScreen()
        # Otherwise passwords do not match
        else:
            heading2 = Label(root, text="Passwords do not match")
            heading2.pack()

    savepwd_btn = Button(root, text="Save Password", padx=15, pady=5, command=checkPasswords)
    savepwd_btn.pack()




# When the application is loaded check if masterpassword table contains a password
check = cursor.execute("SELECT * FROM masterpassword")
accts.commit()
conn.commit()
# If masterpassword already contains a password redirect user to loginScreen
if cursor.fetchall():
    loginScreen()
# Otherwise this is applications first run the user needs to set a password redirect user to firstScreen
else:
    firstScreen()


# Call the window
root.mainloop()