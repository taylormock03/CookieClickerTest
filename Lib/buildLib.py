from tkinter import ttk
from tkinter import *
from Classes.Building import Building
from Lib.miscLib import disableButton, enableButton

# Creates all the building objects
def initBuildings(player, TICKSPEED):
    buildList=[]

    buildList.append(Building(0,"Cursor",1,0.1*(TICKSPEED/1000),player))
    buildList.append(Building(1,"Grandma",100,1*(TICKSPEED/1000),player))
    buildList.append(Building(2,"Farm",1100,8*(TICKSPEED/1000),player))
    buildList.append(Building(3,"Mine",12000,47*(TICKSPEED/1000),player))

    return buildList

# Creates all the buttons for each building
def initBuildButtons(tk, buildList):
    

    list = []
    for Building in buildList:
        list.append(Button(tk, text=str(Building), command=Building.buyBuilding))

    rowNo = 0
    for Building in list:

        Building.grid(row=rowNo, column=1, padx="20", pady="20")
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
        



