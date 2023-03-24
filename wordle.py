import PySimpleGUI as sg
import random
available_words = ["hello","crime","jazzy","fuzzy","pizza","clown","cloth"]
font = ("Helvetica", 22)

idx = random.randint(0,6)
word = available_words[idx]

layout = [[sg.Text('WORDLE',font=font)],
         [sg.Text('YOUR GUESS'), sg.InputText(key="entry")],
         [sg.Text()],
         [sg.Button('ENTER'), sg.Button('QUIT')]]
window = sg.Window('Wordle', layout,size=(500,500))

while True:
    event, values = window.read()   
    if values["entry"] == word:
        print("CONGRATULATIONS YOU GUESSED THE WORD!")
     
    if event == sg.WIN_CLOSED or event == 'QUIT':
        break

window.close()


