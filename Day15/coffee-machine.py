from menu import MENU, resources

isMachineOn = True
resources["money"] = 0

def isEnoughResources(request):
    response = "Sorry there is not enough"
    # Check Espresso
    if(request == "espresso"):
        if (resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]):
            return True
        if(resources["water"] < MENU["espresso"]["ingredients"]["water"]):
            response += " water"
        if (resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]):
            response += " coffee"
        return print(response)
    #  Check Latte
    if (request == "latte"):
        if (resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=
                MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >=
                MENU["latte"]["ingredients"]["milk"]):
            return True
        if (resources["water"] < MENU["latte"]["ingredients"]["water"]):
            response += " water"
        if (resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]):
            response += " coffee"
        if (resources["milk"] < MENU["latte"]["ingredients"]["milk"]):
            response += " milk"
        return print(response)
#  Check Cappuiuccino
    if (request == "cappuccino"):
        if (resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >=
                MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >=
                MENU["cappuccino"]["ingredients"]["milk"]):
            return True
        if (resources["water"] < MENU["cappuccino"]["ingredients"]["water"]):
            response += " water,"
        if (resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]):
            response += " coffee,"
        if (resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]):
            response += " milk."
        return print(response)


def getCoins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

def isEnoughCoins(request, totalCoins):
    if totalCoins >= MENU[request]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def processTransaction(request, totalCoins):
    resources["money"] += MENU[request]["cost"]
    if totalCoins > MENU[request]["cost"]:
        difference = totalCoins -  MENU[request]["cost"]
        print(f'Here is ${format(difference, ".2f")} dollars in change')
    return resources["money"]

def makeCoffee(request):
    # Make Espresso
    if (request == "espresso"):
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f'Here is your espresso ☕')
    #  Make Latte
    if (request == "latte"):
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        print(f'Here is your latte ☕')
    #  Make Cappuiuccino
    if (request == "cappuccino"):
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print(f'Here is your cappuccino ☕')
    return resources

def processRequest(request):
    enoughResources = isEnoughResources(request)
    if(enoughResources):
        totalCoins = getCoins()
        enoughCoins = isEnoughCoins(request, totalCoins)
        if(enoughCoins):
            processTransaction(request, totalCoins)
            makeCoffee(request)

while isMachineOn:
    request = input("What would you like?: (espresso/latte/cappuccino) " ).lower()

    #   Turn of the machine
    if(request == "off"):
        isMachineOn = False

    #   Check request
    if(request == "report"):
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    else:
        processRequest(request)