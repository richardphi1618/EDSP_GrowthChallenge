import PySimpleGUI as sg
from random import randint
window, previous_total, dice, total = None, -1, [] , 0

while True:         #Main Dice Rolling Loop

    sg.theme('dark grey 9')
    
    die = [6]*6

    layout = [
    [sg.Column([dice])],
    [sg.Image(filename=r'./images/{}.png'.format(die[col]), size=(250,250)) for col in range(6)],
    [sg.Text('Number of Dice:')],
    [sg.Button('Roll Dice', bind_return_key=True)],
    [sg.Button(f'Hold Die {col+1}') for col in range(6)],
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