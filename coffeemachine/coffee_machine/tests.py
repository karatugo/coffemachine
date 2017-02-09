from django.test import TestCase
from .DrinkMaker import DrinkMaker


class UnitTest(TestCase):

    def test_tea(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T::", 0.4), {
                         "Drink": "Tea", "Sugar": "0", "Stick": "N"})

    def test_coffee(self):
        drinkMaker = DrinkMaker()

        self.assertEqual(drinkMaker.getDrink("C::", 0.6), {
                         "Drink": "Coffee", "Sugar": "0", "Stick": "N"})

    def test_chocolate(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("H::", 0.5), {
                         "Drink": "Chocolate", "Sugar": "0", "Stick": "N"})

    def test_not_chocolate(self):
        drinkMaker = DrinkMaker()
        self.assertNotEqual(drinkMaker.getDrink(
            "T::", 0.4), {"Drink": "Chocolate", "Sugar": "0", "Stick": "N"})

    def test_tea_sugar(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T:1:0", 0.4), {
                         "Drink": "Tea", "Sugar": "1", "Stick": "Y"})

    def test_tea_twosugar(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T:2:0", 0.4), {
                         "Drink": "Tea", "Sugar": "2", "Stick": "Y"})

    def test_message(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink(
            "M:message-content"), {"Message": "message-content"})

    def test_tea_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T::", 0.4), {
                         "Drink": "Tea", "Sugar": "0", "Stick": "N"})

    def test_tea_no_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T::", 0.3), {
                         "Message": "At least 0.4 € required."})

    def test_tea_too_much_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("T:2:", 40), {
                         "Drink": "Tea", "Sugar": "2", "Stick": "Y"})

    def test_orange_juice(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("O::", 0.6), {
                         "Drink": "Orange Juice", "Sugar": "0", "Stick": "N"})

    def test_orange_juice_no_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("O::", 0.1), {
                         "Message": "At least 0.6 € required."})

    def test_orange_juice_too_much_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("O:2:", 60), {
                         "Drink": "Orange Juice", "Sugar": "2", "Stick": "Y"})

    def test_coffee_extra_hot(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("Ch::", 0.6), {
                         "Drink": "Extra Hot Coffee", "Sugar": "0", "Stick": "N"})

    def test_chocolate_extra_hot(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("Hh:1:", 0.6), {
                         "Drink": "Extra Hot Chocolate", "Sugar": "1", "Stick": "Y"})

    def test_chocolate_extra_hot_no_money(self):
        drinkMaker = DrinkMaker()
        self.assertEqual(drinkMaker.getDrink("Hh:1:", 0.1), {
                         "Message": "At least 0.5 € required."})

    def test_amounts_sold(self):
        drinkMaker = DrinkMaker()

        drinkMaker.getDrink("Hh:1:", 0.6)
        self.assertEqual(drinkMaker.getReport(), {
                         "T": 0, "C": 0, "H": 1, "O": 0})

        drinkMaker.getDrink("T::", 0.4)
        self.assertEqual(drinkMaker.getReport(), {
                         "T": 1, "C": 0, "H": 1, "O": 0})

        drinkMaker.getDrink("O::", 45)
        self.assertEqual(drinkMaker.getReport(), {
                         "T": 1, "C": 0, "H": 1, "O": 1})

        drinkMaker.getDrink("C::", 45)
        self.assertEqual(drinkMaker.getReport(), {
                         "T": 1, "C": 1, "H": 1, "O": 1})

        drinkMaker.getDrink("C::", 0)
        self.assertEqual(drinkMaker.getReport(), {
                         "T": 1, "C": 1, "H": 1, "O": 1})

    def test_earned_money(self):
        drinkMaker = DrinkMaker()

        drinkMaker.getDrink("Hh:1:", 0.6)
        drinkMaker.getDrink("T::", 0.4)
        drinkMaker.getDrink("O::", 45)
        drinkMaker.getDrink("C::", 45)
        drinkMaker.getDrink("C::", 0)
        self.assertEqual(drinkMaker.calculateEarnedMoney(), 2.1)

    def test_no_water(self):
        drinkMaker = DrinkMaker(0, 100)
        self.assertEqual(drinkMaker.getDrink("T::", 0.4), {
                         "Message": "Not enough water/milk."})

    def test_no_milk(self):
        drinkMaker = DrinkMaker(90, 0)
        self.assertEqual(drinkMaker.getDrink("T::", 0.4), {
                         "Message": "Not enough water/milk."})
