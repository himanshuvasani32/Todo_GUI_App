import PySimpleGUI as sg
from converter_function import feet_inches_converter

theme = sg.theme('Black')

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
meter_output = sg.Text("", key="output")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, exit_button, meter_output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = feet_inches_converter(feet, inches)
                window["output"].update(value=f"{feet} feet and {inches} inches is equal to {result} meters.")
            except ValueError:
                sg.popup('Please provide two numbers.', font=('Helvetica', 15))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()