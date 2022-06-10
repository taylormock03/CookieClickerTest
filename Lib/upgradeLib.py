from tkinter import Button
from Classes.Upgrade import Upgrade
from Lib.miscLib import disableButton, enableButton

def initUpgrades(player):
    list = []

    # Cursor Upgrades
    list.append(Upgrade("Reinforced index finger", [-1,0], "%", 200, 100, player))
    list.append(Upgrade("Carpal tunnel prevention cream", [-1,0], "%", 200, 100, player))

    # Grandma Upgrades
    list.append(Upgrade("Forwards from grandma", [1], "%", 200, 100, player))

    # Farm Upgrades
    list.append(Upgrade("Cheap hoes", [2], "%", 200, 100, player))

    return list

def initUpgradeButtons(tk, upgrades):
    i = 0
    upgradeList = []
    for upgrade in upgrades:
        upgradeList.append(Button(tk, text =str(upgrade)))
        upgradeList[i]['command']=lambda idx=i, binst = upgradeList[i]: [upgrade.buyUpgrade(), selfDestruct(idx, binst, upgrades, upgradeList)]
        upgradeList[i].grid(row=i, column=2)
        i+=1
    return upgradeList

def calculateUpgrades(upgradesList, buttonList, player):

    i = 0
    for upgrade in upgradesList:
        if i>= len(buttonList):
            break
        if upgrade.cost > player.money:
            disableButton(buttonList, i)
        else:
            enableButton(buttonList, i)
        
        
        i+=1

def selfDestruct(idx, binst, upgradeList, buttonList):
    buttonList.remove(binst)
    binst.destroy()
    
