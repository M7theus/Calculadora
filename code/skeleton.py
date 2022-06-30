import PySimpleGUI as sg

sg.theme('LightGrey1')
sg.set_options(font = 'Franklin 14', button_element_size = (6,3))

layout = [[sg.Input(size = (49,40))],
          [sg.Button('E', size = (20,0)),sg.Button('C',size = (20,0))],
          [sg.Button('7',size = (7,0)),sg.Button('8',size = (7,0)), sg.Button('9', size = (7,0)),sg.Button('*',size = (7,0))],
          [sg.Button('4',size = (7,0)),sg.Button('5',size = (7,0)), sg.Button('6', size = (7,0)),sg.Button('/',size = (7,0))],
          [sg.Button('1',size = (7,0)),sg.Button('2',size = (7,0)), sg.Button('3', size = (7,0)),sg.Button('-',size = (7,0))],
          [sg.Button('0', size = (20,0)),sg.Button('.', size = (7,0)),sg.Button('+', size = (7,0))]
          ]

window = sg.Window('Calculator',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()