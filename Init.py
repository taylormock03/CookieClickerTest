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

Label(tk, text="Money").grid(row=0, column=0, padx="20", pady="5")
moneyLbl = Label(tk, text="0")
moneyLbl.grid(row=1, column=0, padx="20", pady="20")

Label(tk, text="Cookies per Second").grid(row=2, column=0, padx="20", pady="5")
cpsLbl = Label (tk)
cpsLbl.grid(row=3, column=0, padx="20", pady="20")

Button(tk, text="Cookie", command= player.click).grid(row=4, column=0, padx="20", pady="20")

buildings = initBuildings(player, TICKSPEED)
buildButtons = initBuildButtons(tk, buildings)
player.addBuildings(buildings)

upgrades = initUpgrades(player)

upgradeButtons = initUpgradeButtons(tk, upgrades)


# main loop updated every 100ms
while True:
    tk.after(TICKSPEED,player.calculateMoney(moneyLbl))
    tk.after(0,calculateBuildings(buildings, buildButtons, player))
    tk.after(0,calculateUpgrades(upgrades, upgradeButtons, player))
    tk.after(0, player.calculateCps(cpsLbl, TICKSPEED))
    tk.update()
