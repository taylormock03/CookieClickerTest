from tkinter import *

def disableButton(buttonList, id):
    buttonList[id]["state"] = DISABLED

def enableButton(buttonList, id):
    # print(buttonList[id]["state"])
    if not buttonList[id]["state"] == NORMAL:
        buttonList[id]["state"] = NORMAL
