# Rock Paper Scissor Game using tkinter module 
# Author: Bikram Purkait 

# importing module
from tkinter import *
import random
from PIL import ImageTk,Image
# initializing user and player score
user_scr=0
com_scr=0
# create a function called game  
def game(user):
    # Declare global variable
    global user_scr
    global com_scr
    #generate random no and store it in randno 
    randno=random.randint(1,3)
    # showing choose of computer
    if(randno==1):
        com_choose.config(text="Computer Choose--  Rock")
    elif(randno==2):
        com_choose.config(text="Computer Choose--  Paper")
    else:
        com_choose.config(text="Computer Choose--  Scissor")

    # check winner
    if(randno==1 and user==1) or (randno==2 and user==2) or (randno==3 and user==3) :
        winner_label.config(text="Tie",font="Helvetica 15 bold")
    elif(user==1 and randno==3) or (user==2 and randno==1) or (user==3 and randno==2):
        user_scr+=1
        user_score.config(text="User Score --  " + str(user_scr))
        winner_label.config(text="Yahh!  You Win",font="Helvetica 15 bold")
    else:
        com_scr+=1
        com_score.config(text="Computer Score --  " + str(com_scr))
        winner_label.config(text="Oh!!  Computer Win",font="Helvetica 15 bold")

if __name__ == "__main__":
    # start main application
    # creating the application
    root=Tk()
    # Title
    root.title("Rock-Paper-Scissor Game")
    # set the geometry
    root.config(bg='lemonchiffon')
    # set the icon
    root.iconphoto(True, PhotoImage(file="icon.png"))
    # set the window non resizable
    root.resizable(False,False)


    # Heading
    heading=Label(root,text="Rock-Paper-Scissor Game",font="Helvetica 20 bold",fg='brown4',bg='lemonchiffon')
    heading.pack(padx=10,pady=5,ipadx=10,ipady=5)
    winner_label=Label(text="Lets, Play the game together...",font="Helvetica 15 bold",fg='seagreen',bg='lemonchiffon')
    winner_label.pack(padx=10,pady=5,ipadx=10,ipady=5)


    #  User Choice
    # creating frame for button for Rock,Paper and Scissor 
    frame=Frame(root,bg='lemonchiffon')
    frame.pack(pady=5,ipadx=90,ipady=5)

    heading=Label(frame,text="Choose Any One : ",font="Helvetica 15 bold",fg='purple',bg='lemonchiffon')
    heading.grid(padx=10,pady=5,ipadx=10,ipady=5)

    btn1=Button(frame,text="Rock",command=lambda: game(1),width = 10, bd = 3, bg = 'gold',relief=RAISED,font="Helvetica 12 bold")
    btn1.grid(row=2,column=1,pady=5,ipady=5,padx=20)

    btn1=Button(frame,text="Paper",command=lambda: game(2),width = 10, bd = 3, bg = 'tomato',relief=RAISED,font="Helvetica 12 bold")
    btn1.grid(row=2,column=3,pady=5,ipady=5,padx=20)

    btn1=Button(frame,text="Scissor",command=lambda: game(3),width = 10, bd = 3, bg = 'turquoise1',relief=RAISED,font="Helvetica 12 bold")
    btn1.grid(row=2,column=5,pady=5,ipady=5,padx=20)



    # Score
    # creating frame for scoretable
    s_frame=Frame(root,bg='lemonchiffon')
    s_frame.pack(pady=5,ipady=5,anchor=NW)

    # heading for scoreboard
    heading=Label(s_frame,text="Scoreboard",font="Helvetica 15 bold",fg='deeppink2',bg='lemonchiffon')
    heading.grid(pady=5,ipady=5,padx=10,ipadx=10)

    # label for user score , computer score , computer choose 
    user_score=Label(s_frame,text="User Score -- ",font="Helvetica 15 bold",fg='coral',bg='lemonchiffon')
    user_score.grid(row=1,column=20)

    com_score=Label(s_frame,text="Computer Score -- ",font="Helvetica 15 bold",fg='coral',bg='lemonchiffon')
    com_score.grid(row=2,column=20)

    com_choose=Label(s_frame,text="",font="Helvetica 15 bold",fg='coral',bg='lemonchiffon')
    com_choose.grid(row=3,column=20)


    # infinite loop for application run
    root.mainloop()
    # close main application