import PySimpleGUI as sg
from random import randint
from PIL import Image, ImageTk
import YahtzeeScore as YS
import os

window, previous_total, total = None, -1 , 0
dice = [6]*5
rerolls = [0]*5
dice_img = []
ScoreLogged = False
turn = 0
CurrentScore = 0

cwd = os.getcwd()

ScoreCard_Options = ["ones", "twos", "threes", "fours", "fives", "sixes", "Three of a Kind", \
                        "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]

for i in range(len(dice)):
    dice_img += [sg.Image(filename=f'./images/{dice[i]}.png', size=(200,200), key= f'_DieImage{i}_', tooltip = f'Die {i+1}')]

def LaunchScoreWindow():
    layout = [[sg.Text('The second window')],
              [sg.Listbox(ScoreCard_Options, enable_events=True, size=(30,15), k='ScoreOptions')],
              [sg.Button('Accept', k='LogScore')]]
    return sg.Window('Second Window', layout, finalize=True)

def load_image(path, window, frame):
    try:
        image = Image.open(path)
        image.thumbnail((250, 250))
        photo_img = ImageTk.PhotoImage(image)
        window[frame].update(data=photo_img)
    except Exception as e:
        print(f"Unable to open {path}!")
        print(f"error: {e}")

sg.theme('dark grey 9')
layout = [
[sg.Text('Controls:')],
[sg.Button(f'Hold Die {col+1}') for col in range(5)],
[sg.Button('Roll Dice', bind_return_key=True)],
[sg.Text('  3 ',size=(3,1), key='_TOTAL_', font='ANY 20', text_color = 'red')],
[sg.Text(f'Turn {turn}', key = "_Turn_")],
[sg.Column([dice_img])],
]

window = sg.Window('Dice Roller', layout).Finalize()

while True:         #Main Dice Rolling Loop

    if previous_total != total:
        window.Element('_TOTAL_').Update(total)
        window.Element('_Turn_').Update(f"Turn: {turn}")
        
        for i in range(len(dice)): 
            load_image(f'./images/{dice[i]}.png',window, f'_DieImage{i}_')
    
    if turn >= 3:
        print("round over")
        ScoreWindow = LaunchScoreWindow()
        while ScoreLogged != True:      # Loop to log score
            event, values = ScoreWindow.Read()
            print(event)
            print(values)
            if event == sg.WIN_CLOSED or event == "LogScore":
                print ("Closed Score")
                print (f"final dice: {dice}")

                CurrentScore = YS.Check(values, dice, CurrentScore)
                
                turn = 0
                total = 0
                dice = [6]*5
                rerolls = [0]*5     
                ScoreLogged = True

                for i in range(len(dice)):
                    dice_img += [sg.Image(filename=f'{cwd}/images/{dice[i]}.png', size=(200,200), key= f'_DieImage{i}_', tooltip = f'Die {i+1}')]
                
                window.Element('_TOTAL_').Update(total)
                window.Element('_Turn_').Update(f"Turn: {turn}")

                for i in range(len(dice)): 
                    load_image(f'./images/{dice[i]}.png',window, f'_DieImage{i}_')

                print (f"Current Score: {CurrentScore}")
                
                ScoreCard_Options.remove(values['ScoreOptions'][0])
                
                ScoreWindow.close()

    else:
        ScoreLogged = False
                    
    while True:      # Loop to read # dice to roll, create list of images
        event, values = window.Read()

        if event is None:
            exit()
        else:
            print(event)

        total = 0
        old_dice = dice

        if event == "Roll Dice":
            for i in range(len(dice)):           # for each die rolled, get the random # and build list of images
                if rerolls[i] == 0:
                    val = randint(1,6)
                    dice[i] = val
                else:
                    dice[i] = old_dice[i]

                total += dice[i]
                dice_img += [sg.Image(filename=f'./images/{dice[i]}.png', size=(250,250), key= f'_DieImage{i}_')]   
            turn += 1

            print(turn)
            print(dice)

            break

        if "Hold Die" in event and turn > 0:
            hold_val = int(event[-1])
            if rerolls[hold_val-1] == 1:
                rerolls[hold_val-1] = 0
            elif rerolls[hold_val-1] == 0:
                rerolls[hold_val-1] = 1
            print(rerolls)
        

        
            
