from tkinter import *

root = Tk()

accounts = {"Usernames": [], "Passwords": []}

master_pwd = "test"


def loginScreen():
    root.geometry("250x100")
    root.title("Account Vault | Sign in")

    title = Label(root, text="Enter Master Password")
    title.config(anchor=CENTER)
    title.pack()

    pwd_entry = Entry(root, show="*", width=20)
    pwd_entry.pack()


    def accountVault():
        for widget in root.winfo_children():
            widget.destroy()


        root.geometry("600x600")
        root.title("Account Vault")

        title = Label(root, text="Account Vault")
        title.config(anchor=CENTER)
        title.pack()


        def printAccounts():
            pwds = accounts["Passwords"]
            users = accounts["Usernames"]

            heading = Label(root, text="Usernames in order")
            heading.config(anchor=CENTER)
            heading.pack()

            heading1 = Label(root, text="Passwords in order")

            user_lbl = Label(root, text=users)
            user_lbl.config(anchor=CENTER)
            user_lbl.pack()

            space = Label(root, text="\n")
            space.config(anchor=CENTER)
            space.pack()

            heading1.pack()

            pwd_lbl = Label(root, text=pwds)
            pwd_lbl.config(anchor=CENTER)
            pwd_lbl.pack()

            space1 = Label(root, text="\n")
            space1.config(anchor=CENTER)
            space1.pack()



        def addAccount():
            for widget in root.winfo_children():
                widget.destroy()

            root.geometry("350x150")
            root.title("Account Vault | Add Account")

            heading = Label(root, text="Enter Username")
            heading.pack()

            username_entry = Entry(root, width=20)
            username_entry.pack()

            heading1 = Label(root, text="Enter Password")
            heading1.pack()

            password_entry = Entry(root, width=20)
            password_entry.pack()


            def saveAccount():
                pwd = password_entry.get()
                username = username_entry.get()

                accounts["Usernames"].append("." + username + "\n")
                accounts["Passwords"].append("." + pwd + "\n")

                accountVault()


            submit = Button(root, text="Save", padx=15, pady=5, command=saveAccount)
            submit.pack()


        def deleteAccount():
            for widget in root.winfo_children():
                widget.destroy()

            root.geometry("350x150")
            root.title("Account Vault | Delete Account")

            title = Label(root, text="enter the number of the account to delete 1-x")
            title.config(anchor=CENTER)
            title.pack()

            delete_ent = Entry(root, width=5)
            delete_ent.pack()

            def submitDelete():
                if delete_ent.get() == "1":
                    accounts["Usernames"].pop(0)
                    accounts["Passwords"].pop(0)
                elif delete_ent.get() == "2":
                    accounts["Usernames"].pop(1)
                    accounts["Passwords"].pop(1)
                elif delete_ent.get() == "3":
                    accounts["Usernames"].pop(2)
                    accounts["Passwords"].pop(2)
                elif delete_ent.get() == "4":
                    accounts["Usernames"].pop(3)
                    accounts["Passwords"].pop(3)
                elif delete_ent.get() == "5":
                    accounts["Usernames"].pop(4)
                    accounts["Passwords"].pop(4)
                elif delete_ent.get() == "6":
                    accounts["Usernames"].pop(5)
                    accounts["Passwords"].pop(5)

                accountVault()


            btn = Button(root, text="delete", padx=15, pady=5, command=submitDelete)
            btn.config(anchor=CENTER)
            btn.pack()


        add_btn = Button(root, text="Add Account", padx=15, pady=5, command=addAccount)
        add_btn.place(x=120, y=550)

        delete_btn = Button(root, text="Delete Account", padx=15, pady=5, command=deleteAccount)
        delete_btn.place(x=350, y=550)

        printAccounts()


    def checkMasterPwd():
        if pwd_entry.get() == master_pwd:
            accountVault()
            print("Login Successful")
        else:
            wrong = Label(root, text="Incorrect Password")
            wrong.pack()


    submit = Button(root, text="Submit", padx=15, pady=5, command=checkMasterPwd)
    submit.pack()


loginScreen()
root.mainloop()