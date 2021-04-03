import PySimpleGUI as sg
from random import randint
window, previous_total, dice, total = None, -1, [] , 0

while True:         #Main Dice Rolling Loop

    sg.theme('dark grey 9')
    
    die = [6]*6
    dice_img = []

    for i in range(len(die)):
        dice_img += [sg.Image(filename=f'./images/{i+1}.png', size=(250,250), key= f'_DieImage{i}_')]

    layout = [
    [sg.Column([dice_img])],
    [sg.Text('Controls:')],
    [sg.Button(f'Hold Die {col+1}') for col in range(6)],
    [sg.Button('Roll Dice', bind_return_key=True)],
    [sg.Text('   ',size=(3,1), key='_TOTAL_', font='ANY 20', text_color = 'red')],]

    if previous_total != total:
        window.Close() if window is not None else None
        window = sg.Window('Dice Roller', layout).Finalize()
    window.Element('_TOTAL_').Update(total)

    while True:                             # Loop to read # dice to roll, create list of images
        event, values = window.Read()

        if event is None:
            exit()
        else:
            print(event)

        total = 0
        if event == "Roll Dice":
            for i in range(len(die)):           # for each die rolled, get the random # and build list of images
                val = randint(1,6)
                die[i] = val
                dice_img += [sg.Image(filename=f'./images/{die[i]}.png', size=(250,250), key= f'_DieImage{i}_')]
                total += die[i]
            
            for i in range(len(die)):
                window.Element(f'_DieImage{i}_').Update(dice_img[i])
            break
