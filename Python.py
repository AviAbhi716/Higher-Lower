import random
import HL_logo
import HL_database
import os
def display(details):
    name=details["name"]
    country=details["country"]
    batting=details["batting_style"]
    return f"{name}, {country}, {batting}"
score=0
def compare(choose,run1,run2):
    if run1<run2:
        if choose==1:
            return False
        else:
            return True
    else:
        if choose==1:
            return True
        else:
            return False
game=True
details1 = random.choice(HL_database.cricketers_data)
while game:
    print(HL_logo.game_logo)
    details2 = random.choice(HL_database.cricketers_data)
    print(f"Compare1: {display(details1)}")
    print(HL_logo.vs)
    print(f"Compare2: {display(details2)}")
    guess=int(input("Who has more runs: '1' or '2':"))
    runs1=details1["runs"]
    runs2=details2["runs"]
    check=compare(guess,runs1,runs2)
    if check is True:
        score+=1
        os.system('cls')
        details1=details2
        runs1=runs2
        print(f"You are right. Your score is: {score}")
    else:
        game=False
        os.system('cls')
        print(f"You are wrong...Your final score is {score}")

