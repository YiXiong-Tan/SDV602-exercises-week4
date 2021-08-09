
import random
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

sg.theme('Dark Blue 3')

title = 'Adventure Game!'

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

def update_result_of_layout4(result,dice_result):
    layout = make_layout('layout4')
    
    #update layout
    if result == 'WIN':
        layout[1] = [sg.Text(f'CONGRATULATIONS! DICE ROLL {dice_result}! YOU WIN!')]
    elif result == 'LOSE':
        print('LOSE')
        layout[1] = [sg.Text(f'DICE ROLL {dice_result}! YOU DIED!')]

    return layout

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

layout = make_layout('layout1')
window = sg.Window(title, layout)
event, values = window.read()

while True:
    
    print(event)
    if event == sg.WIN_CLOSED or event == '_no_':
        break
    
    # 2nd phase
    if event == '_go_to_mountains_':
        window.close()
        layout = make_layout('layout2')
        window = sg.Window(title, layout)
        event, values = window.read()
    
    if event == '_go_to_castle_':
        window.close()
        layout = make_layout('layout3')
        window = sg.Window(title, layout)
        event, values = window.read()
    
    # 3rd phase
    if event == '_fight_':
        window.close()
        
        #get result
        result, dice_result = dice_roll('hard')

        
        #update layout
        layout = update_result_of_layout4(result, dice_result)
        window = sg.Window(title, layout)
        
        event, values = window.read()
        
    if event == '_eat_':
        window.close()
        
        #get result
        result, dice_result = dice_roll('easy')

        #update layout
        layout = update_result_of_layout4(result, dice_result)
        window = sg.Window(title, layout)
        event, values = window.read()
    
    # restart page
    if event == '_yes_':
        window.close()
        layout = make_layout('layout1')
        window = sg.Window(title, layout)
        event, values = window.read()

window.close()