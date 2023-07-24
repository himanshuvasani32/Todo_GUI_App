import PySimpleGUI as sg
from converter_function import feet_inches_converter

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
meter_output = sg.Text("", key="output")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, meter_output]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = feet_inches_converter(feet, inches)
    window["output"].update(value=f"{feet} feet and {inches} inches is equal to {result} meters.")

window.close()