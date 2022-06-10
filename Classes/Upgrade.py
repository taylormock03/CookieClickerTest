from sqlalchemy import null


class Upgrade:
    name = ""

    # This gives the id of the building it effects. -1 = player's click
    affectedBuilding = []
    # Percentage increase or base increase
    effect = None
    # How big of an increase
    magnitude = 0

    cost = 0

    player = None


    def __init__(self, name, affectedBuilding, effect, magnitude, cost, player) -> None:
        self.name = name
        self.affectedBuilding = affectedBuilding
        self.effect = effect
        self.magnitude = magnitude
        self.cost = cost
        self.player = player

    def calculateEffect(self, moneyOutput):
        if self.effect == "%":
            return moneyOutput * self.magnitude

        # This will change
        elif self.effect == "+":
            return moneyOutput + self.magnitude

    def buyUpgrade(self):
        self.player.money -= self.cost
        self.player.upgrades.append(self)

    def __str__(self) -> str:
        if self.effect == "%":
            if len(self.affectedBuilding) ==1:
                return self.name + " +" +str(self.magnitude) +"% increase to " + self.player.buildings[self.affectedBuilding[0]].name
            else: 
                return self.name + " +" +str(self.magnitude) +"% increase to " + self.player.buildings[self.affectedBuilding[1]].name