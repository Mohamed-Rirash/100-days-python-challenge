from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()






is_on = True

while is_on:
    option = menu.get_items()
    choose = input(f"what would you like ? ({option})").lower()
    if choose == "off":
        is_on = False
    elif choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
       