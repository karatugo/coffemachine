from .BeverageQuantityChecker import BeverageQuantityChecker


class DrinkMaker:

    drinkTypes = ["T", "C", "H", "O"]
    prices = {"T": 0.4, "C": 0.6, "H": 0.5, "O": 0.6}

    def __init__(self, water=100, milk=100):
        self.totalAmountsSold = {"T": 0, "C": 0, "H": 0, "O": 0}
        self.water = water
        self.milk = milk
        self.drink = ""

    def getDrink(self, order, money=0):

        if(BeverageQuantityChecker.isEmpty(self.water, self.milk)):
            return {"Message": "Not enough water/milk."}

        parameters = order.split(":")
        if(parameters[0] == "M"):
            return {"Message": parameters[1]}

        self.drink = parameters[0]
        extraHot = self.setExtraHot(self.drink)

        price = self.prices[self.drink]
        result = {}

        if (self.drink == "T" and money >= price):
            result = {"Drink": "Tea"}
        elif(self.drink == "C" and money >= price):
            result = {"Drink": "Coffee"}
        elif(self.drink == "H" and money >= price):
            result = {"Drink": "Chocolate"}
        elif(self.drink == "O" and money >= price):
            result = {"Drink": "Orange Juice"}
        elif(price > money):
            return {"Message": "At least " + str(self.prices[self.drink]) + " € required."}
        else:
            return {"Message": "No drink found."}

        self.totalAmountsSold[
            self.drink] = self.totalAmountsSold[self.drink] + 1

        if(extraHot):
            result["Drink"] = "Extra Hot " + result["Drink"]

        sugar = parameters[1]
        if(sugar == ""):
            result['Sugar'] = "0"
            result['Stick'] = "N"
        else:
            result['Sugar'] = sugar
            result['Stick'] = "Y"

        return result

    def getReport(self):
        return self.totalAmountsSold

    def calculateEarnedMoney(self):
        money = 0
        for dt in self.drinkTypes:
            money += self.totalAmountsSold[dt] * self.prices[dt]

        return money

    def setExtraHot(self, drink):
        if(drink.endswith("h")):
            self.drink = drink[:1]
            return True

        return False
