
class Player:
    money = 0
    upgrades =[]
    buildings = []

    def __init__(self) -> None:
        self.money = 0
        self.upgrades = []
        self.buildings = []

    def addBuildings(self,buildings):
        self.buildings = buildings

    # Calculates how much money the player earns
    def calculateMoney(self, moneyLbl):
        for building in self.buildings:
            self.money+= building.calculateOutput() 

        self.money= round(self.money,2)
        moneyLbl.config(text=str(self.money))
        
    def click(self):
        self.money+=1

    def calculateCps(self, cpsLbl, TICKSPEED):
        cps = 0
        for building in self.buildings:
            cps+= building.calculateCps(TICKSPEED)
        cpsLbl.config(text= str(round(cps,1)))