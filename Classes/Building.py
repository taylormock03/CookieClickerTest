import math

from Lib.miscLib import filterUpgrades


class Building:
    name = ""
    baseCost = 0
    production = 0
    id = 0
    quantity = 0
    player = None

    def __init__(self, id, name, cost, production, player) -> None:
        self.id = id
        self.name = name
        self.baseCost = cost
        self.production = production
        self.player = player
        self.quantity = 0

    def buyBuilding(self):
        self.player.money -= self.calculateCost()
        self.quantity+=1

    def calculateCost(self):
        return math.ceil(self.baseCost* 1.15**self.quantity)

    def calculateOutput(self, upgrades):
        output = self.production* self.quantity
        for x in upgrades:
            output = x.calculateEffect(output)

        return output

    def calculateCps(self, TICKSPEED, player):
        return self.calculateOutput(filterUpgrades(self,player.upgrades)) * (1000/TICKSPEED)

    def __str__(self) -> str:
        return self.name + " x" + str(self.quantity) + ": $" + str(self.calculateCost())