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

def UpdateScore():
    L1['text'] = str(root.score1)
    L2['text'] = str(root.score2)

def TennisScore():
    
    if (root.counter1 == root.counter2):
        root.score1 = "ALL"
        root.score2 = "ALL"
    else:
        root.score1 = str(root.counter1)
        root.score2 = str(root.counter2)
    
    if (root.counter1 == 0):
        root.score1 = "Love"
    if (root.counter2 == 0):
        root.score2 = "Love"

        

L1 = Label(root.counter1, text="Love")
L1.pack()
b1 = Button(root, text="Point Player 1", command=input1)
b1.pack()

L2 = Label(root.counter2, text="Love")
L2.pack()
b2 = Button(root, text="Point Player 2", command=input2)
b2.pack()

TennisScore()
UpdateScore()

root.mainloop()