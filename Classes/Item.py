import math


class Item:
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

    def buyItem(self):
        self.player.money -= self.calculateCost()
        self.quantity+=1

    def calculateCost(self):
        return math.ceil(self.baseCost* 1.15**self.quantity)

    def calculateOutput(self):
        return self.production* self.quantity

    def calculateCps(self, TICKSPEED):
        return self.calculateOutput() * (1000/TICKSPEED)

    def __str__(self) -> str:
        return self.name + " x" + str(self.quantity) + ": $" + str(self.calculateCost())