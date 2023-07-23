import functions
import PySimpleGUI as sg

label = sg.Text("Add a new to-do here")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window("To-do app", layout=[[label], [input_box, add_button]])
window.read()
window.close()