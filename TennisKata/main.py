from tkinter import *
root = Tk()

#variable is stored in the root object
root.counter = [0]*3
root.score = [0]*3

SCORE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}

def input1():
    root.counter[1] += 1
    print(f"Player1: {root.counter[1]}")
    TennisScore()
    UpdateScore()
    
def input2():
    root.counter[2] += 1
    print(f"Player2: {root.counter[2]}")
    TennisScore()
    UpdateScore()

def input3():
    root.counter[1] = 0
    root.counter[2] = 0
    print('reset')
    TennisScore()
    UpdateScore()

def UpdateScore():
    L1['text'] = str(root.score[1])
    L2['text'] = str(root.score[2])

def TennisScore():
    
    for i in range(3):
        if root.counter[i] <= 3 :
            root.score[i] = SCORE[root.counter[i]]

    if (root.counter[1] == root.counter[2] and root.counter[1] > 0 and root.counter[2] > 0) :
        root.score[1] = f"{root.score[1]}-ALL"
        root.score[2] = f"{root.score[2]}-ALL"
    
    if (root.counter[1] == root.counter[2] and root.counter[1] >= 3) :
        root.score[1] = "Deuce"
        root.score[2] = "Deuce"
    
    if (root.counter[1] >= 3 and root.counter[2] >= 3 and root.counter[1] > root.counter[2]):
        root.score[1] = "Advantage"
        root.score[2] = "-"
        
    if(root.counter[1] >= 3 and root.counter[2] >= 3 and root.counter[1] < root.counter[2]):
        root.score[1] = "-"
        root.score[2] = "Advantage"

    if (root.counter[1] >= 4 and root.counter[1] > root.counter[2]+1):
        root.score[1] = "winner"
        root.score[2] = "loser"
    if (root.counter[2] >= 4 and root.counter[1]+1 < root.counter[2]):
        root.score[1] = "loser"
        root.score[2] = "winner"      


if __name__ == "__main__":

    root.geometry("265x100")
    root.title("Tennis ScoreCard")
    
    L1 = Label(root.score[1], text="Love")
    L1.grid(row=1, column=1, padx=10, pady=5)
    b1 = Button(root, text="Point Player 1", command=input1)
    b1.grid(row=2, column=1, padx=10, pady=5)

    L2 = Label(root.score[2], text="Love")
    L2.grid(row=1, column=2, padx=10, pady=5)
    b2 = Button(root, text="Point Player 2", command=input2)
    b2.grid(row=2, column=2, padx=10, pady=5)

    b3 = Button(root, text="reset", command=input3)
    b3.grid(row=1, column=3, padx=10, pady=10)

    TennisScore()
    UpdateScore()

    root.mainloop()