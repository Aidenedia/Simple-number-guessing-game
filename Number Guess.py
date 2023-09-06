import random
import os
import time
True_False = True
answered = False
os.system("cls")
print("""
▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ 　 ▒█▀▄▀█ ▒█░░▒█ 　 ▒█▄░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ 　 ░▒█░░ ▒█░░▒█ 　 ▒█▒█▒█ ▒█▄▄▄█ 　 ▒█▒█▒█ ▒█░▒█ ▒█▒█▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ 　 ░▒█░░ ▒█▄▄▄█ 　 ▒█░░▒█ ░░▒█░░ 　 ▒█░░▀█ ░▀▄▄▀ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█ 

▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 
▒█░▄▄ ▒█░▒█ ▒█▀▀▀ ░▀▀▀▄▄ ░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ▒█░▄▄ 　 ▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀ 
▒█▄▄█ ░▀▄▄▀ ▒█▄▄▄ ▒█▄▄▄█ ▒█▄▄▄█ ▄█▄ ▒█░░▀█ ▒█▄▄█ 　 ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄""")

time.sleep(3)
os.system("cls")

print("""
▀█▀ █░█ █▀▀   █▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█   █ █▀   █░█ █▀█   ▀█▀ █▀█   ▄█ █▀█ █▀█ █▀█ ░
░█░ █▀█ ██▄   █░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄   █ ▄█   █▄█ █▀▀   ░█░ █▄█   ░█ █▄█ █▄█ █▄█ ▄

█▀▀ █▀█ █▀█ █▀▄ █░░ █░█ █▀▀ █▄▀ █
█▄█ █▄█ █▄█ █▄▀ █▄▄ █▄█ █▄▄ █░█ ▄""")

time.sleep(3)
os.system("cls")

while True_False == True:
    try:
        number = random.randrange(0,1001)
        answered = False
        while answered == False:
            answer = int(input("What number?\n"))
            if answer > number:
                os.system("cls")
                print("Your number is bigger than the answer.")
            if answer < number:
                os.system("cls")
                print("Your number is smaller than the answer.")
            elif answer == number:
                os.system("cls")
                print("You won! Congratulations.")
                again = input("Would you like to go again? (y/n)\n").lower()
                if again == "y":
                    os.system("cls")
                    answered = True
                else:
                    True_False = False
                    break
    except ValueError:
        os.system("cls")
        print("It needs to be a number.")
        continue
