from tkinter import *
from tkinter import ttk
from Classes.Player import Player
from Lib.buildLib import *
from Lib.upgradeLib import *

# how many ms between each game tick
TICKSPEED = 100

tk = Tk()
tk.title("Cookie Clicker")



player = Player()

# Money Frame
moneyFrame = Frame(tk)
moneyFrame.grid(row=0, column=0)
Label(moneyFrame, text="Money").pack()
moneyLbl = Label(moneyFrame, text="0")
moneyLbl.pack()

Label(moneyFrame, text="Cookies per Second").pack()
cpsLbl = Label (moneyFrame)
cpsLbl.pack()

Button(moneyFrame, text="Cookie", command= player.click).pack()


# Buildings
buildings = initBuildings(player, TICKSPEED)
buildButtons = initBuildButtons(tk, buildings)
player.addBuildings(buildings)

# Upgrades
upgrades = initUpgrades(player)
upgradeButtons = initUpgradeButtons(tk, upgrades)


# main loop updated every 100ms
while True:
    tk.after(TICKSPEED,player.calculateMoney(moneyLbl))
    tk.after(0,calculateBuildings(buildings, buildButtons, player))
    tk.after(0,calculateUpgrades(upgrades, upgradeButtons, player))
    tk.after(0, player.calculateCps(cpsLbl, TICKSPEED))
    tk.update()
