from tkinter import ttk
from tkinter import *
from Classes.Item import Item

# Creates all the building objects
def initBuildings(player, TICKSPEED):
    buildList=[]

    buildList.append(Item(0,"Cursor",1,0.1*(TICKSPEED/1000),player))
    buildList.append(Item(1,"Grandma",100,1*(TICKSPEED/1000),player))
    buildList.append(Item(2,"Farm",1100,8*(TICKSPEED/1000),player))

    return buildList

# Creates all the buttons for each building
def initUpgradeList(tk, buildList):
    

    list = []
    for item in buildList:
        list.append(Button(tk, text=str(item), command=item.buyItem))

    rowNo = 0
    for item in list:

        item.grid(row=rowNo, column=1, padx="20", pady="20")
        rowNo+=1
   
    return list

# Checks if new building can be bought and updates the quantity and price of the building
def calculateBuildings(buildingList, buttonList, player):

    i = 0
    for building in buildingList:
        if building.calculateCost() > player.money:
            disableButton(buttonList, building.id)
        else:
            enableButton(buttonList, building.id)
        
        buttonList[i].config(text=str(building))
        i+=1
        



def disableButton(buttonList, id):
    buttonList[id]["state"] = DISABLED

def enableButton(buttonList, id):
    buttonList[id]["state"] = NORMAL
