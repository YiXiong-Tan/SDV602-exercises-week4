
import random
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

"""
Goal here is to explore and start using PySimpleGUI to get more hands-on. 
The game here has a similar concept as the previous exercise.
"""

sg.theme('Dark Blue 3')
title = 'Adventure Game!'

"""
Taken from the last exercise. 
It's great that I've a function that I could reuse instead of creating another one.
Saved me some time.
This function is to simulate a dice roll
"""
def dice_roll(level):

    result = ''
    value = 0

    # generate a random number between 1-5
    # if level is easy, you will win when the number generated is 3 or below
    # if level is hard, you will win when the number generated is 2 or below

    if(level == 'easy'):
        value = random.randint(1,5)
        
        if(value <= 3):
            result = 'WIN'
        else:
            result = 'LOSE'
    
    elif(level == 'hard'):
        value = random.randint(1,5)
        if(value <= 2):
            result = 'WIN'
        else:
            result = 'LOSE'
    
    # call loading procedure to add a bit of suspends during the dice roll
    print(f'\nDice roll:{value} from 5\n')

    return result, value


"""
Since we cannot reuse a layout in PySimpleGUI, 
I've created a function that returns the layout type required everytime a window needs to be shown.
This function accepts the layout type, then returns the layout specified.
"""
def make_layout(layout_type):
    
    layout = []

    if layout_type == 'layout1':
        layout = [[sg.Text('You are in the forest.. \nWhich way do you want to go?')],
                [sg.Button('Left to the Mountains', key='_go_to_mountains_'), sg.Button('Right to the Castle',key='_go_to_castle_')]]
    elif layout_type == 'layout2':
        layout = [[sg.Text('You are in the Mountains.. \nWhat do you want to do?')],
                [sg.Button('Fight dragons', key='_fight_'), sg.Button('Eat berries',key='_eat_')]]
    elif layout_type == 'layout3':
        layout = [[sg.Text('You are in the Castle.. \nWhat do you want to do?')],
            [sg.Button('Conquer Castle', key='_fight_'), sg.Button('Have a feast',key='_eat_')]]
    elif layout_type == 'layout4':
        layout = [[sg.Text('GAME OVER')],
                [sg.Text(key='_result_')],
                [sg.Text('RESTART?')],
                [sg.Button('YES',key='_yes_'),sg.Button('NO',key='_no_')]]

    return layout

"""
Layout4 will have a different text based on whether the player wins or loses.
This function is to change the layout result
"""
def make_layout4_and_update_result(result,dice_result):
    layout = make_layout('layout4')
    
    #update layout
    if result == 'WIN':
        layout[1] = [sg.Text(f'CONGRATULATIONS! DICE ROLL {dice_result}! YOU WIN!')]
    elif result == 'LOSE':
        layout[1] = [sg.Text(f'DICE ROLL {dice_result}! YOU DIED!')]

    return layout

# initialize the window
# shows the 1st phase of the game
layout = make_layout('layout1')
window = sg.Window(title, layout)
event, values = window.read()

while True:
    
    print(event)
    if event == sg.WIN_CLOSED or event == '_no_':
        break
    
    # ------2nd phase of the game-------
    if event == '_go_to_mountains_':
        #close the previous window before starting a new one
        window.close()
        
        layout = make_layout('layout2')
        window = sg.Window(title, layout)
        event, values = window.read()
    
    if event == '_go_to_castle_':
        window.close()
        layout = make_layout('layout3')
        
        window = sg.Window(title, layout)
        event, values = window.read()
    
    # ------3rd phase of the game-------
    if event == '_fight_':
        window.close()
        
        # roll dice
        result, dice_result = dice_roll('hard')
        
        #update layout
        layout = make_layout4_and_update_result(result, dice_result)
        
        window = sg.Window(title, layout)
        event, values = window.read()
        
    if event == '_eat_':
        window.close()
        
        # roll dice
        result, dice_result = dice_roll('easy')

        #update layout
        layout = make_layout4_and_update_result(result, dice_result)
        window = sg.Window(title, layout)
        event, values = window.read()
    
    # --------go to the 1st phase-----
    if event == '_yes_':
        window.close()
        layout = make_layout('layout1')
        window = sg.Window(title, layout)
        event, values = window.read()

window.close()