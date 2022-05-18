from tkinter import *
import random
from PIL import Image, ImageTk

rock = "R"
paper = "P"
scissors = "S"

User = 1
Tie = 0
Comp = -1

global cp_score
global user_score

cp_score = 0
user_score = 0
game_count = 0

choices = [rock, paper, scissors]

root = Tk()

user_rock_img = ImageTk.PhotoImage(Image.open("imgs/rps-icons.png"))
user_paper_img = ImageTk.PhotoImage(Image.open("imgs/paper.png"))
user_scissor_img = ImageTk.PhotoImage(Image.open("imgs/scissors.png"))
cp_rock_img = ImageTk.PhotoImage(Image.open("imgs/rps-icons.png"))
cp_paper_img = ImageTk.PhotoImage(Image.open("imgs/paper.png"))
cp_scissor_img = ImageTk.PhotoImage(Image.open("imgs/scissors.png"))

banner_img = ImageTk.PhotoImage(Image.open("imgs/rps-banner.png"))


def screen():
    cp_score = 0
    user_score = 0

    root.geometry("600x400")
    root.title("Rock Paper Scissors")
    root.config(bg="PURPLE")

    banner = Label(root, image=banner_img, bg="PURPLE")
    banner.config(anchor=CENTER)
    banner.pack()

    cp_score_lbl = Label(root, text="CP Score: ", bg="PURPLE")
    cp_score_lbl.place(x=470, y=370)

    user_score_lbl = Label(root, text="Your Score: ", bg="PURPLE")
    user_score_lbl.place(x=30, y=370)

    user_choice_img = Label(root, image=user_rock_img, bg="PURPLE", width=80, height=80)
    user_choice_img.place(x=40, y=200)

    cp_choice_img = Label(root, image=cp_rock_img, bg="PURPLE", width=80, height=80)
    cp_choice_img.place(x=450, y=200)


    def get_cp_choice():
        global cp_choice
        cp_choice = random.choice(choices)
        if cp_choice == rock:
            cp_choice_img.config(image=cp_rock_img)
        elif cp_choice == paper:
            cp_choice_img.config(image=cp_paper_img)
        elif cp_choice == scissors:
            cp_choice_img.config(image=cp_scissor_img)
        return cp_choice


    def play_game(button_clicked):
        if button_clicked == None:
            pass
        elif button_clicked == rock:
            get_cp_choice()
            user_choice_img.config(image=user_rock_img)
        elif button_clicked == paper:
            get_cp_choice()
            user_choice_img.config(image=user_paper_img)
        elif button_clicked == scissors:
            get_cp_choice()
            user_choice_img.config(image=user_scissor_img)

        msg = Label(root) # You Win
        msg1 = Label(root) # You Lose
        msg2 = Label(root) # Tie Game


        if button_clicked == rock and cp_choice == scissors:
            msg1.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg.config(text="Winner", bg="PURPLE", fg="GREEN", font=150)
            msg.place(x=270, y=180)
            winner = User
            return winner
        elif button_clicked == rock and cp_choice == paper:
            msg.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg1.config(text="Loser !", bg="PURPLE", fg="RED", font=150)
            msg1.place(x=270, y=180)
            winner = Comp
            return winner
        elif button_clicked == paper and cp_choice == rock:
            msg1.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg.config(text="Winner", bg="PURPLE", fg="GREEN", font=150)
            msg.place(x=270, y=180)
            winner = User
            return winner
        elif button_clicked == paper and cp_choice == scissors:
            msg.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg1.config(text="Loser !", bg="PURPLE", fg="RED", font=150)
            msg1.place(x=270, y=180)
            winner = Comp
            return winner
        elif button_clicked == scissors and cp_choice == paper:
            msg1.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg.config(text="Winner", bg="PURPLE", fg="GREEN", font=150)
            msg.place(x=270, y=180)
            winner = User
            return winner
        elif button_clicked == scissors and cp_choice == rock:
            msg.config(fg="PURPLE")
            msg2.config(fg="PURPLE")
            msg1.config(text="Loser !", bg="PURPLE", fg="RED", font=150)
            msg1.place(x=270, y=180)
            winner = Comp
            return winner
        elif button_clicked == rock and cp_choice == rock:
            msg.config(fg="PURPLE")
            msg1.config(fg="PURPLE")
            msg2.config(text="Draw!!", bg="PURPLE", fg="BLACK", font=150)
            msg2.place(x=270, y=180)
            winner = Tie
            return winner
        elif button_clicked == paper and cp_choice == paper:
            msg.config(fg="PURPLE")
            msg1.config(fg="PURPLE")
            msg2.config(text="Draw!!", bg="PURPLE", fg="BLACK", font=150)
            msg2.place(x=270, y=180)
            winner = Tie
            return winner
        elif button_clicked == scissors and cp_choice == scissors:
            msg.config(fg="PURPLE")
            msg1.config(fg="PURPLE")
            msg2.config(text="Draw!!", bg="PURPLE", fg="BLACK", font=150)
            msg2.place(x=270, y=180)
            winner = Tie
            return winner


    def get_btn_rock():
        button_clicked = rock
        play_game(button_clicked)


    def get_btn_paper():
        button_clicked = paper
        play_game(button_clicked)



    def get_btn_scissors():
        button_clicked = scissors
        play_game(button_clicked)






    rock_btn = Button(root, text="ROCK", bg="GREY", command=get_btn_rock)
    rock_btn.place(x=170, y=350)
    paper_btn = Button(root, text="PAPER", bg="GREY", command=get_btn_paper)
    paper_btn.place(x=270, y=350)
    scissors_btn = Button(root, text="SCISSORS", bg="GREY", command=get_btn_scissors)
    scissors_btn.place(x=370, y=350)

    if play_game == 1:
        winner = User
    elif play_game == -1:
        winner = Comp
    elif play_game == 0:
        winner = Tie
    else:
        winner = None

    if winner == 1:
        user_score += 1
    elif winner == 0:
        print("Tie")
    elif winner == -1:
        cp_score += 1

    if rock_btn:
        print(cp_score, user_score)
    if paper_btn:
        print(cp_score, user_score)
    if scissors_btn:
        print(cp_score, user_score)






screen()
root.mainloop()