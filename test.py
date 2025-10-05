import time
import os

def shutdown_computer():
    # This will initiate a shutdown after 1 second
    os.system("shutdown /s /t 1")

def main():
    choice = int(input("Do you want to play a game?\n1. Yes\n2. No\nYour choice: "))
    if choice == 1:
        print(f"Thank you for choosing to play a game with me.")
        time.sleep(5)
        exit()
    elif choice == 2:
        print("Too bad. You never had a choice. Goodbye!")
        time.sleep(2)
        shutdown_computer()
        exit()

main()


