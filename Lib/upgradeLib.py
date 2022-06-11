from tkinter import *
from Classes.Upgrade import Upgrade
from Lib.miscLib import disableButton, enableButton

def initUpgrades(player):
    list = []

    # Cursor Upgrades
    list.append(Upgrade("Reinforced index finger", 0, "%", 200, 100, player))
    list.append(Upgrade("Carpal tunnel prevention cream", 0, "%", 200, 500, player))

    # Grandma Upgrades
    list.append(Upgrade("Forwards from grandma", 1, "%", 200, 1000, player))

    # Farm Upgrades
    list.append(Upgrade("Cheap hoes", 2, "%", 200, 1100, player))
    list.append(Upgrade("Cheaper hoes", 2, "%", 200, 1100, player))

    return list

def initUpgradeButtons(tk, upgradeList):
    
    upgradeFrame = LabelFrame(tk, text="Upgrades", padx=15, pady=15)    
    upgradeFrame.grid(row=0, column=2)

    upgradeCanvas = Canvas(upgradeFrame, scrollregion=(0,0,1000,1000), width= 500)

    upgradeSb = Scrollbar(upgradeFrame, orient='vertical')
    upgradeSb.pack(side = RIGHT, fill=Y)
    upgradeSb.config(command=upgradeCanvas.yview)

    upgradeCanvas.config(yscrollcommand= upgradeSb.set)
    upgradeCanvas.pack(side=LEFT, expand=True, fill=BOTH)
    
    
    upgradeButtonList = []
    i=0
    for upgrade in upgradeList:
        upgradeButtonList.append(Button(upgradeCanvas, text =str(upgrade)))
        upgradeButtonList[i]['command']= lambda upgradex=upgrade, idx=i, binst = upgradeButtonList[i]: [upgradex.buyUpgrade(),  selfDestruct(idx, binst, upgradeList, upgradeButtonList)]
        i+=1

    rowNo = 0
    for upgrade in upgradeButtonList:

        upgrade.pack(side=TOP, pady=10)
        upgradeCanvas.create_window(0, rowNo, anchor='nw', window=upgrade)
        rowNo+=50

    return upgradeButtonList

def calculateUpgrades(upgradesList, buttonList, player):

    i = 0
    for upgrade in upgradesList:
        if i> len(buttonList):
            break
        if upgrade is None:
            i+=1
            continue
        if upgrade.cost > player.money:
            disableButton(buttonList, i)
        else:
            enableButton(buttonList, i)
        
        
        i+=1

def selfDestruct(idx, binst, upgradeList, buttonList):
    buttonList[idx]= None
    upgradeList[idx] = None
    binst.destroy()
    
