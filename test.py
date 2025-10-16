import time
import os

#
### Questionaire
#

def choice():
    while True:
        print("Are you gay?")
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

#
### This will initiate a shutdown after 1 second
#

def shutdown_computer():
    os.system("shutdown /s /t 1")

#
### Main function
#

def main():
    user_choice = choice()
    if user_choice == 1:
        print("Aye man, i knew it all along.")
        print("Don't go choking on cock now.")
        time.sleep(5)
        exit()
    elif user_choice == 2:
        print("Bitch stop lying")
        time.sleep(5)
        shutdown_computer()
        exit()

main()
