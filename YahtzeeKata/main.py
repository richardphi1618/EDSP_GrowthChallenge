import PySimpleGUI as sg
from random import randint
from PIL import Image, ImageTk
window, previous_total, total = None, -1 , 0
dice = [6]*5
rerolls = [0]*5
dice_img = []

turn = 0

for i in range(len(dice)):
    dice_img += [sg.Image(filename=f'./images/{dice[i]}.png', size=(200,200), key= f'_DieImage{i}_', tooltip = f'Die {i+1}')]

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
        if turn >= 1:
            for i in range(len(dice)): 
                load_image(f'./images/{dice[i]}.png',window, f'_DieImage{i}_')
                    
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
        
            
