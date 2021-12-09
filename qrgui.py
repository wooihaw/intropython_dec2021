# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:02:46 2021

@author: wooihaw
"""
# Create a GUI for QR code generator

import PySimpleGUI as sg
import pyqrcode

layout = [
    [sg.Text('Enter text to be encoded')],
    [sg.InputText(key='-IN-')],
    [sg.Button('Generate'), sg.Button('Save', disabled=True), sg.Button('Exit')],
    [sg.Image(key='-IMG-')]
    ]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event in ['Exit', sg.WIN_CLOSED]:
        break
    if event == 'Generate':
        text = values['-IN-']
        qr = pyqrcode.create(text)
        window['-IMG-'].update(data=qr.png_as_base64_str(scale=5))
        window['Save'].update(disabled=False)

window.close()