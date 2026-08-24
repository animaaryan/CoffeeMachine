# Import functions
import menu
import resources as report

# Prompt user by asking what they want
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

# Constants
REPORT = report.resources

# Turn off the Coffee Machine if user enters "off"
if user_choice == "off":
    print("Turning off the machine...")

# Print the report of what's available
if user_choice == "report":
    for key in REPORT:
        print(f"{key}: {REPORT[key]} ml")