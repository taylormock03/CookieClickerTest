from tkinter import *

def disableButton(buttonList, id):
    buttonList[id]["state"] = DISABLED

def enableButton(buttonList, id):
    # print(buttonList[id]["state"])
    if not buttonList[id]["state"] == NORMAL:
        buttonList[id]["state"] = NORMAL

def filterUpgrades(building, upgrades):
    buildingId = building.id

    filteredUpgrades = []
    for x in upgrades:
        if x.affectedBuilding == buildingId:
            filteredUpgrades.append(x)
    return filteredUpgrades


def clickUpgrades(upgrades):
    filteredUpgrades = []
    for x in upgrades:
        if x.affectedBuilding == 0:
            filteredUpgrades.append(x)
    return filteredUpgrades
