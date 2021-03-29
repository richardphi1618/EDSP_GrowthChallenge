from tkinter import *
root = Tk()

#variable is stored in the root object
root.counter1 = 0
root.counter2 = 0
root.score1 = "Love"
root.score2 = "Love"

def input1():
    root.counter1 += 1
    print(root.counter1)
    TennisScore()
    UpdateScore()
    
def input2():
    root.counter2 += 1
    print(root.counter2)
    TennisScore()
    UpdateScore()

def input3():
    root.counter1 = 0
    root.counter2 = 0
    print('reset')
    TennisScore()
    UpdateScore()

def UpdateScore():
    L1['text'] = str(root.score1)
    L2['text'] = str(root.score2)

def TennisScore():
    
    if (root.counter1 == 0):
        root.score1 = "Love"
    if (root.counter2 == 0):
        root.score2 = "Love"

    if (root.counter1 == 1):
        root.score1 = "15"
    if (root.counter2 == 1):
        root.score2 = "15"
    
    if (root.counter1 == 2):
        root.score1 = "30"
    if (root.counter2 == 2):
        root.score2 = "30"
    
    if (root.counter1 == 3):
        root.score1 = "40"
    if (root.counter2 == 3):
        root.score2 = "40"

    if (root.counter1 == root.counter2 and root.counter1 > 0 and root.counter2 > 0) :
        root.score1 = f"{root.score1}-ALL"
        root.score2 = f"{root.score2}-ALL"
    
    if (root.counter1 == root.counter2 and root.counter1 >= 3) :
        root.score1 = "Deuce"
        root.score2 = "Deuce"
    
    if (root.counter1 >= 3 and root.counter2 >= 3 and root.counter1 > root.counter2):
        root.score1 = "Advantage"
        root.score2 = "-"
    if(root.counter1 >= 3 and root.counter2 >= 3 and root.counter1 < root.counter2):
        root.score1 = "-"
        root.score2 = "Advantage"

    if (root.counter1 >= 4 and root.counter1 > root.counter2+1):
        root.score1 = "winner"
        root.score2 = "loser"
    if(root.counter2 >= 4 and root.counter1+1 < root.counter2):
        root.score1 = "loser"
        root.score2 = "winner"      


if __name__ == "__main__":

    root.geometry("300x100+200+200")

    L1 = Label(root.counter1, text="Love")
    L1.grid(row=1, column=0, padx=20, pady=10)
    b1 = Button(root, text="Point Player 1", command=input1)
    b1.grid(row=2, column=0, padx=10, pady=10)

    L2 = Label(root.counter2, text="Love")
    L2.grid(row=1, column=1, padx=20, pady=10)
    b2 = Button(root, text="Point Player 2", command=input2)
    b2.grid(row=2, column=1, padx=10, pady=10)

    b3 = Button(root, text="reset", command=input3)
    b3.grid(row=2, column=3, padx=20, pady=10)

    TennisScore()
    UpdateScore()

    root.mainloop()