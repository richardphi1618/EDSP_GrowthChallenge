from RomanNumerals import RomanNumeral as RN
import PySimpleGUI as sg    

# Layout                                                         # Creat GUI
layout = [[sg.Txt(''  * 10)],                      
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='Black', key='input')],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('c'), sg.ReadFormButton('«')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('÷')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')], 
          [sg.ReadFormButton('RN')],
          ]

# Set PySimpleGUI
form = sg.FlexForm('13411_CALCULATOR', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Set Process
Equal = ''
List_Op_Error =  ['+','-','*','/','(']

# Loop
while True:
    button, value = form.Read()                            # call GUI
    
    # Press Button
    if button == 'c':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button == '«':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-().':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button == 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button == '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    elif button == 'RN':
        num = int(Equal)
        RomanNumeral = RN(num)
        sg.popup_ok("The Roman Numeral is: \n" + RomanNumeral.RN)

    
   # Process Conditional
    elif button == '=':
        # Error Case
        for i in List_Op_Error :  
            if '*' == Equal[0] or '/' == Equal[0] or ')' == Equal[0]  or i == Equal[-1]:   # Check Error Case
                Answer = "Error Operation" 
                break
            elif Equal == '6001012630187':
                Answer = 'Apisit.Khomcharoen'
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error Operation" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error Operation" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error Operation" 
                    break
    # Calculate Case    
        else :
            Answer = str("%0.2f" %(eval(Equal)))                         # eval(Equal)  
            if '.0' in Answer:
                Answer = str(int(float(Answer)))                         # convert float to int
        form.FindElement('input').Update(Answer)                         # Update to GUI
        Equal = Answer

    elif button == 'Quit'  or button is None:                            # QUIT Program
        break