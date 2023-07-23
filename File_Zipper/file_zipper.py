import PySimpleGUI as sg
from make_zip import make_archive

label1 = sg.Text("Select files to compress:")
input_box1 = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination Folder:")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Zipper",
                   [[label1, input_box1, choose_button1],
                    [label2, input_box2, choose_button2],
                    [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()