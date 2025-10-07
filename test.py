import time
import os

def choice():
    while True:
        print("Do you want to play a game?")
        print("1. Yes")
        print("2. No")
        try:
            user_choice = int(input("Your choice: "))
            if user_choice in [1, 2]:
                return user_choice
            else:
                print("Invalid choice. Please enter 1 or 2.\n")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).\n")

def shutdown_computer():
    # This will initiate a shutdown after 1 second
    os.system("shutdown /s /t 1")

def main():
    user_choice = choice()
    if user_choice == 1:
        print("Thank you for choosing to play a game with me.")
        print("Have a good day ig.")
        time.sleep(5)
        exit()
    elif user_choice == 2:
        print("Too bad. You never had a choice. Goodbye!")
        time.sleep(2)
        shutdown_computer()
        exit()

main()
