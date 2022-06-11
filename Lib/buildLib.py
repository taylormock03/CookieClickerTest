from tkinter import ttk
from tkinter import *
from Classes.Building import Building
from Lib.miscLib import disableButton, enableButton

# Creates all the building objects
def initBuildings(player, TICKSPEED):
    buildList=[]

    buildList.append(Building(0,"Cursor",15,0.1*(TICKSPEED/1000),player))
    buildList.append(Building(1,"Grandma",100,1*(TICKSPEED/1000),player))
    buildList.append(Building(2,"Farm",1100,8*(TICKSPEED/1000),player))
    buildList.append(Building(3,"Mine",12000,47*(TICKSPEED/1000),player))
    

    return buildList

# Creates all the buttons for each building
def initBuildButtons(tk, buildList):

    buildFrame = LabelFrame(tk, text="Buildings", padx=15, pady=15)    
    buildFrame.grid(row=0, column=1)

    buildCanvas = Canvas(buildFrame, scrollregion=(0,0,1000,1000), width= 200)

    buildSb = Scrollbar(buildFrame, orient='vertical')
    buildSb.pack(side = RIGHT, fill=Y)
    buildSb.config(command=buildCanvas.yview)

    buildCanvas.config(yscrollcommand= buildSb.set)
    buildCanvas.pack(side=LEFT, expand=True, fill=BOTH)

    buttonList = []
    
    for Building in buildList:
        buttonList.append(Button(buildCanvas, text=str(Building), command=Building.buyBuilding))



    rowNo = 0
    for Building in buttonList:

        Building.pack(side=TOP, pady=10)
        buildCanvas.create_window(0, rowNo, anchor='nw', window=Building)
        rowNo+=50
        
    
    return buttonList

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
        



