MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# step 4 check if resources are sufficient
# this will take the order ingredients as an input and work on it

# function to make sure the order ingredients aren't more than the resources available
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    # for each loop
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            # if there are not enough resources, return false
            return False
    # if there are enough resources, we will return true
    return True

# this will not take an input
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    # the total will be returned
    return total

# make sure user inserted enough for their drink
# this will take an input for money recieved and cost of drink

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        # round the change my two decimal places
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # profit is global so we must invoke it with global
        global profit
        profit += drink_cost
        # return true when payment is accepted
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        # return false when payment is insufficient
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    # get hold of order ingredients and loop through them
    for item in order_ingredients:
        # subtract order ingredients from resources
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

# prompt the user to ask what they like
# step 1
# since the prompt should show every time an action is completed I will use a while loop
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    # step 2
    # turn off the coffee machine when choice == 'off'
    if choice == "off":
        is_on = False
    # step 3
    # when a user choose report - print out a detailed report of the resources remaining
    # water, milk, coffee, and money
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # step 5
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
