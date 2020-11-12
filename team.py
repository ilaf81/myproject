# function to handles team building
import hero
import time
import random

import os
def spend_TP_menu():
    print(" --Spending Training--")
    print("[1] Position 1")
    print("[2] Position 2")
    print("[3] Position 3")
    print("[4] Position 4")
    print("[5] Show Training Points")
    print("[0] Back\n")


def shop_menu():
    print(" --Menu Shop--")
    print("[1] Buy Def Candy - 100")
    print("[2] Buy M Def Candy - 100")
    print("[3] Buy HP Potion- 100")
    print("[4] Buy Hero")
    print("[5] Sell Artifacts - 5000")
    print("[0] Back\n")

def welcome_message():
    print("""
    Welcome to Anime Arena
    Gather heroes and battle on the Anime Arena.
    Reach the top floor at the Babel Tower and become the strongest.
    \n\n""")

# function to show hero information
def hero_information_menu():
    print(" --Menu Hero--")
    print("[1] Search")
    print("[0] Back\n")

# function for training
def training_menu():
    print(" --Menu Training--")
    print("[1] Train Strength")
    print("[2] Train Intellect")
    print("[3] Train Speed")
    print("[4] Quest")
    print("[5] Spend Training Points")
    print("[0] Back\n")
def strength_training(str_point):
    print(" Welcome to the Gym. You have to do 10 push up to earn 1 str point\n")
    for x in range(0, 11):
        print(x)
        print("Down")
        print("UP")
        time.sleep(1.5)
    str_point += 1
    print(f"You have earn 1 str training point and now have {str_point} strength points ")
    time.sleep(2)
    return str_point

def speed_training(spd_point):
    print(" Welcome to the Beach. You have to run 10 miles to earn 1 speed point\n")
    mile = 0
    for x in range(0, 11):
        miles_list = ["No Sweat", "Better yet", "Just for you", "Just for me", "Give me more", "I'm alive", "Just for kicks", "I'm in heaven","It feels great", "Right on time", "Let's do it again"]
        print(x)

        print("Mile")
        print(miles_list[mile])
        time.sleep(1.5)
        mile += 1
    spd_point += 1
    print(f"You have earn 1 str training point and now have {spd_point} strength points\n")
    time.sleep(2)
    return spd_point

def intellect_training(int_point):
    print(" Welcome to the IQ Club. Think of a number 1-100 to earn 1 int point\n")
    response = 0
    for x in range(0, 9):
        guess_list = ["Add 8", "Multiply by 6", "Add 6", "Take away 3", "Add 12", "Take away 15", "Divide by 6", "Take away the number you choose", "The number you thinking is 8"]

        print(guess_list[response])
        time.sleep(1.5)
        response += 1
    int_point += 1
    print(f"You have earn 1 int training point and now have {int_point} intellect points\n")
    time.sleep(2)
    return int_point

def quest_training(stamina_points):
    print(" Welcome to the Quest Kiosk. You can spend 10 stamina to get 100 training points of your choice.")
    print(f"You currently have {stamina_points} stamina points")
    print("You have an 75% chance to complete the quest. If you failed, no training points")
    print("Would you like to play?(yes/no)")
    quest_answer = input().strip().lower()
    if quest_answer == "yes" and stamina_points >= 10:
        quest = random.randint(1, 100)
        if quest <= 75:
            print("You completed the quest and earn 100 training points")
            earned_point = 100

            return earned_point
        else:
            print("You failed the quest")
            return 0
    elif quest_answer == "no":
        print("See you later")
        return -1
    else:
        print("You don't have enough stamina. Conduct training to increase your stamina")
        return -1

def spend_P1():
    print(" --Position 1--")
    print("[1] Train Strength")
    print("[2] Train Intellect")
    print("[3] Train Speed")
    print("[4] Train HP")
    print("[5] Train Defense")
    print("[6] Train M Defense")
    print("[7] Show Stats")
    print("[0] Back\n")

def spend_P2():
    print(" --Position 1--")
    print("[1] Train Strength")
    print("[2] Train Intellect")
    print("[3] Train Speed")
    print("[4] Train HP")
    print("[5] Train Defense")
    print("[6] Train M Defense")
    print("[7] Show Stats")
    print("[0] Back\n")

def spend_P3():
    print(" --Position 1--")
    print("[1] Train Strength")
    print("[2] Train Intellect")
    print("[3] Train Speed")
    print("[4] Train HP")
    print("[5] Train Defense")
    print("[6] Train M Defense")
    print("[7] Show Stats")
    print("[0] Back\n")

def spend_P4():
    print(" --Position 1--")
    print("[1] Train Strength")
    print("[2] Train Intellect")
    print("[3] Train Speed")
    print("[4] Train HP")
    print("[5] Train Defense")
    print("[6] Train M Defense")
    print("[7] Show Stats")
    print("[0] Back\n")

def team_display(team1_name,team1, team2_name, team2):

    print(f"""

    {team1_name.center(25,"-")}                            {team2_name.center(25,"-")}
    P4. {team1["heroS3"].ljust(20)}                             P4. {team2["heroS3"].ljust(20)}  
    P3. {team1["heroS2"].ljust(20)}             VS              P3. {team2["heroS2"].ljust(20)} 
    P2. {str(team1["heroS1"]).ljust(20)}                             P2. {team2["heroS1"].ljust(20)} 
    ####################                                 ####################
    P1 {team1["heroM"].ljust(20)}                               P1 {team2["heroM"].ljust(20)} 
    """)

# function to get hero id
def get_hero(id):
    if id == 1:
        hero_obj = hero.Adan()
        return hero_obj
    elif id == 2:
        hero_obj = hero.Franky()
        return hero_obj
    elif id == 3:
        hero_obj = hero.Alma()
        return hero_obj
    elif id == 4:
        hero_obj = hero.Luis()
        return hero_obj
    elif id == 5:
        hero_obj = hero.Chino()
        return hero_obj
    elif id == 6:
        hero_obj = hero.Gil()
        return hero_obj
    elif id == 7:
        hero_obj = hero.Lalo()
        return hero_obj
    elif id == 8:
        hero_obj = hero.Sherman()
        return hero_obj


def heroes_id_converter(h_name):
    heroes_list_id = {"adan": 1, "franky": 2, "alma": 3, "luis": 4, "kakashi": 5, "lee": 6, "itachi": 7, "ino": 8}
    for hero in heroes_list_id.keys():

        if h_name == hero:
            return heroes_list_id[hero]

def set_hero(hero, position, h_list):
    hero_list = h_list
    hero_list.insert(hero,position)

def Game_Menu():
    print(" --Menu--")
    print("[1] Training")
    print("[2] Go to Shop")
    print("[3] Show Team")
    print("[4] Build Team")
    print("[5] Go to Dungeon")
    print("[0] Exit the Game\n")


def team_build_menu():
    print(" --Team Building Menu--")
    print("[1] Edit Position 1")
    print("[2] Edit Position 2")
    print("[3] Edit Position 3")
    print("[4] Edit Position 4")
    print("[5] Hero information")
    print("[0] Back\n")
