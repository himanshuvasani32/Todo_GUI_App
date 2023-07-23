import PySimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input], [inches_label, inches_input], [convert_button]])

window.read()
window.close()