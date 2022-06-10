from tkinter import *

def disableButton(buttonList, id):
    buttonList[id]["state"] = DISABLED

def enableButton(buttonList, id):
    buttonList[id]["state"] = NORMAL
