# Import functions
import menu
import resources as report

# Constants
REPORT = report.resources
OUT_OF_RESOURCES = False
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

while not OUT_OF_RESOURCES:

    # Prompt user by asking what they want
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the Coffee Machine if user enters "off"
    if user_choice == "off":
        print("Turning off the machine...")
        OUT_OF_RESOURCES = True

    # Print the report of what's available
    elif user_choice == "report":
        resources()

    # If they select coffee
    elif user_choice == 'espresso' or 'latte' or 'cappuccino':
        print("Please insert coins.")

        # Ask user for coins
        coin_quart = float(input("How many quarters?: "))
        coin_dim = float(input("How many dimes?: "))
        coin_nick = float(input("How many nickles?: "))
        coin_penn = float(input("How many pennies?: "))

        # Store the price of the coffee
        store_value = cost(user_choice)

        # Call function
        money = calc(coin_quart, coin_dim, coin_nick, coin_penn)

        # Print the money
        print(f"Here is ${money - store_value} in change.")

        # Print the choice
        print(f"Here is you {user_choice} ☕ Enjoy!")

    else:
        print("Incorrect choice!")

