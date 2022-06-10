
from Lib.miscLib import clickUpgrades, filterUpgrades


class Player:
    money = 0
    upgrades =[]
    buildings = []

    def __init__(self) -> None:
        self.money = 599
        self.upgrades = []
        self.buildings = []

    def addBuildings(self,buildings):
        self.buildings = buildings

    # Calculates how much money the player earns
    def calculateMoney(self, moneyLbl):
        for building in self.buildings:
            self.money+= building.calculateOutput(filterUpgrades(building, self.upgrades)) 

        self.money= round(self.money,2)
        moneyLbl.config(text=str(self.money))
        
    def click(self):
        addAmt = 1
        for upgrades in clickUpgrades(self.upgrades):
            addAmt = upgrades.calculateEffect(addAmt)
        self.money += addAmt

    def calculateCps(self, cpsLbl, TICKSPEED):
        cps = 0
        for building in self.buildings:
            cps+= building.calculateCps(TICKSPEED, self)
        cpsLbl.config(text= str(round(cps,1)))