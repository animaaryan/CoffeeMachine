# Import functions
import menu
import resources as report
from art import logo

# Print logo
print(logo)

# Constants
REPORT = report.resources
IS_RUNNING = False
ACTIVE_MENU = menu.MENU

# Coins
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
MACHINE_MONEY = 0

# Calculate money
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total +=  int(input("How many dimes?: ")) * 0.1
    total +=  int(input("How many nickles?: ")) * 0.05
    total +=  int(input("How many pennies?: ")) * 0.01
    return total

# Print the resources available
def resources(num):

    # Print the data
    print(f"Water: {REPORT['water']} ml")
    print(f"Milk: {REPORT['milk']} ml")
    print(f"Coffee: {REPORT['coffee']} ml")
    print(f"Money: ${num}")

# Print from the menu
def cost(choice):

    # Pick the cost from the menu
    return ACTIVE_MENU[choice]['cost']

def reduce(selection, resource):
    available = REPORT[resource]
    required = ACTIVE_MENU[selection]['ingredients'][resource]
    REPORT[resource] = available - required

def billing(actual_cost, user_money):
    if user_money >= actual_cost:
        return True
    else:
        print("Insufficient money")
        return False

while not IS_RUNNING:

    # Prompt user by asking what they want
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the Coffee Machine if user enters "off"
    if user_choice == "off":
        print("Turning off the machine...")
        IS_RUNNING = True

    # Print the report of what's available
    elif user_choice == "report":
        resources(MACHINE_MONEY)

    # If they select coffee
    elif user_choice == 'espresso' or user_choice =='latte' or user_choice == 'cappuccino':

        # Store value
        needed_ingredients = ACTIVE_MENU[user_choice]['ingredients']

        # Resources Flag
        is_sufficient = True

        # Reduce ingredients
        for key in needed_ingredients:
            available_ingredients = REPORT[key]

            if available_ingredients < needed_ingredients[key]:
                is_sufficient = False

        if not is_sufficient:
            print("ERR1200: Insufficient Resources")
            continue

        # Store the price of the coffee
        store_value = cost(user_choice)

        # Call function
        user_money = process_coins()

        # Check if the user has enough money for this
        has_money = billing(store_value, user_money)

        if not has_money:
            continue
        else:
            # Add to machine money
            MACHINE_MONEY += store_value

            # Print the money
            print(f"Here is ${round(user_money - store_value, 2)} in change.")

            # Reduce after resources are sufficient
            for key in needed_ingredients:
                reduce(user_choice, key)

            # Print the choice
            print(f"Here is your {user_choice} ☕ Enjoy!")

            # Reset user money
            USER_MONEY = 0

    else:
        print("Incorrect choice!")

