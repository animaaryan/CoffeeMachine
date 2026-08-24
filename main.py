# Import functions
import menu
import resources as report

# Constants
REPORT = report.resources
IS_RUNNING = False
ACTIVE_MENU = menu.MENU

# Coins
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

# Calculate money
def calc(coin_q, coin_d, coin_n, coin_p):
    return round((coin_q * QUARTERS) +
                 (coin_d * DIMES) +
                 (coin_n * NICKLES) +
                 (coin_p * PENNIES), 2)

# Print the resources available
def resources():

    # Print the datat
    for key in REPORT:
        print(f"{key}: {REPORT[key]} ml")

# Print from the menu
def cost(choice):

    # Pick the cost from the menu
    return ACTIVE_MENU[choice]['cost']

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
        resources()

    # If they select coffee
    elif user_choice == 'espresso' or user_choice =='latte' or user_choice == 'cappuccino':
        print("Please insert coins.")

        # Ask user for coins
        coin_quart = int(input("How many quarters?: "))
        coin_dim = int(input("How many dimes?: "))
        coin_nick = int(input("How many nickles?: "))
        coin_penn = int(input("How many pennies?: "))

        # Store the price of the coffee
        store_value = cost(user_choice)

        # Call function
        money = calc(coin_quart, coin_dim, coin_nick, coin_penn)

        # Check if the user has enough money for this
        has_money = billing(store_value, money)

        if has_money:
            continue
        else:
            # Print the money
            print(f"Here is ${round(money - store_value, 2)} in change.")

            # Print the choice
            print(f"Here is you {user_choice} ☕ Enjoy!")

    else:
        print("Incorrect choice!")

