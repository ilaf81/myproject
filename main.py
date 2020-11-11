import hero
import time
import random
import combat
import team

import numpy as np
import string



def combat_stats(hero_s, hero_s2):
    #hero 1 stats
    name1 = hero_s.name
    hp1 = str(hero_s.get_health())
    def1 = str(hero_s.get_defense())
    str1 = str(hero_s.get_strength())
    int1 = str(hero_s.get_intellect())
    spd1 = str(hero_s.get_speed())
    ele1 = hero_s.element
    #hero 2 stats
    name2 = hero_s2.name
    hp2 = str(hero_s2.get_health())
    def2 = str(hero_s2.get_defense())
    str2 = str(hero_s2.get_strength())
    int2 = str(hero_s2.get_intellect())
    spd2 = str(hero_s2.get_speed())
    ele2 = hero_s2.element
    print(f"""
    {name1.ljust(15)}                     {name2.ljust(15)}
    HP: {hp1.ljust(15)}                   HP: {hp2.ljust(15)}
    DEF: {def1.ljust(15)}                  DEF: {def2.ljust(15)} 
    STR: {str1.ljust(15)}                  STR: {str2.ljust(15)} 
    INT: {int1.ljust(15)}                  INT: {int2.ljust(15)} 
    SPD: {spd1.ljust(15)}                  SPD: {spd2.ljust(15)}
    ELM: {ele1.ljust(15)}                  ELM: {ele2.ljust(15)}   
    """)




#defining Enemy Team
def level_1_fire():
    t2lvl1_1 = hero.Chino()
    t2lvl1_2 = hero.Gil()
    t2lvl1_3 = hero.Lalo()
    t2lvl1_4 = hero.Sherman()
    enemy_list = [t2lvl1_1, t2lvl1_2, t2lvl1_3, t2lvl1_4]
    return enemy_list

def battle():

    team.team_display(team1_name,team1, team2_name, team2)
    print("Round 1")
    print(f"{t1hero1.get_name()} and {t2hero1.get_name()} step in for battle")
    time.sleep(2)
    combat_stats(t1hero1, t2hero1)
    #a_move = "kinto_attack"
    if team1_speed >= team2_speed:

        d_hp = combat.standard_attack(t1hero1, t1hero2, t1hero3, t1hero4, t2hero1, team1_name)
        t2hero1.set_health(d_hp)
        time.sleep(3)
        d_hp = combat.standard_attack(t2hero1, t2hero2, t2hero3, t2hero4, t1hero1, team2_name)
        t1hero1.set_health(d_hp)
        time.sleep(3)

    else:
        d_hp = combat.standard_attack(t2hero1, t2hero2, t2hero3, t2hero4, t1hero1, team2_name)
        t1hero1.set_health(d_hp)
        time.sleep(3)
        d_hp = combat.standard_attack(t1hero1, t1hero2, t1hero3, t1hero4, t2hero1, team1_name)
        t2hero1.set_health(d_hp)
        time.sleep(3)
    #team_display()


    print("Round 2")
    combat.reset_round_var(t1hero1, t1hero2, t1hero3, t1hero4)
    combat.reset_round_var(t2hero1, t2hero2, t2hero3, t2hero4)
    combat_stats(t1hero1, t2hero1)
    if t1hero1.get_speed() >= t2hero1.get_speed():

        d_hp = combat.kinto_attack(t1hero1, t1hero2, t1hero3, t1hero4, t2hero1, team1_name)
        t2hero1.set_health(d_hp)
        d_hp = combat.kinto_attack(t2hero1, t2hero2, t2hero3, t2hero4, t1hero1, team2_name)
        t1hero1.set_health(d_hp)
    else:
        d_hp = combat.kinto_attack(t2hero1, t2hero2, t2hero3, t2hero4, t1hero1, team2_name)
        t1hero1.set_health(d_hp)
        d_hp = combat.kinto_attack(t1hero1, t1hero2, t1hero3, t1hero4, t2hero1, team1_name)
        t2hero1.set_health(d_hp)
    print("Would you like to use Kinto attacks")

team.Game_Menu()

option_menu = int(input(" Enter your option >"))

while option_menu != 0:
    if option_menu == 1:
        print("Option 1 was selected")

    elif option_menu == 2:
        print("Option 2 was selected")
    elif option_menu == 3:
        print("Option 3 was selected")
    elif option_menu == 4:
        team.team_build_menu()
        opt_tb_menu = int(input(" Enter your option >"))
        while opt_tb_menu != 0:

            if opt_tb_menu == 1:
                print("Please enter your hero name for position 1")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero1 = team.get_hero(hero_id)
                print(f"You assigned {t1hero1.get_name()} to position 1")

            elif opt_tb_menu == 2:
                print("Please enter your hero name for position 2")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero2 = team.get_hero(hero_id)
                print(f"You assigned {t1hero2.get_name()} to position 2")

            elif opt_tb_menu == 3:
                print("Please enter your hero name for position 3")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero3 = team.get_hero(hero_id)
                print(f"You assigned {t1hero3.get_name()} to position 3")

            elif opt_tb_menu == 4:
                print("Please enter your hero name for position 4")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero4 = team.get_hero(hero_id)
                print(f"You assigned {t1hero4.get_name()} to position 4")

            else:
                print("Invalid option")
            print()
            team.team_build_menu()
            opt_tb_menu = int(input(" Enter your option"))

    elif option_menu == 5:
        print("Option 5 was selected")
        break
    else:
        print("Invalid option")
    print()
    team.Game_Menu()
    option_menu = int(input(" Enter your option"))
#print("Thank you for playing Anime Arena")
#exit()

# defining Team 1
t1hero1 = hero.Adan()
t1hero2 = hero.Alma()
t1hero3 = hero.Franky()
t1hero4 = hero.Luis()

team1_hero_list = [t1hero1, t1hero2, t1hero3, t1hero4]
team1_speed = t1hero1.get_speed() + t1hero2.get_speed() + t1hero3.get_speed() + t1hero4.get_speed()


print(f"team 1 speed is {team1_speed}")
team1 = {"heroM": team1_hero_list[0].name, "heroS1": team1_hero_list[1].name, "heroS2": team1_hero_list[2].name,
         "heroS3": team1_hero_list[3].name}

#defining Enemy Team
level_e_list = level_1_fire()
t2hero1 = level_e_list[0]
t2hero2 = level_e_list[1]
t2hero3 = level_e_list[2]
t2hero4 = level_e_list[3]

team2_hero_list = [t2hero1, t2hero2, t2hero3, t2hero4]
team2_speed = t2hero1.get_speed() + t2hero2.get_speed() + t2hero3.get_speed() + t2hero4.get_speed()
print(f"team 2 speed is {team2_speed}")

team2_speed = t2hero1.get_speed() + t2hero2.get_speed() + t2hero3.get_speed() + t2hero4.get_speed()

team2 = {"heroM": t2hero1.get_name(), "heroS1": t2hero3.get_name(), "heroS2": t2hero4.get_name(),
         "heroS3": t2hero2.get_name()}

team1_name = "ScRuS"
team2_name = "Fire Team 1"


#function to display team information, hero position, and battling hero

def main():
    battle()

main()










# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
