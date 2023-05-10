import PySimpleGUI as sg 

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("Choose")

window = sg.Window("File Compressor", 
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2]])
window.read()
window.close()