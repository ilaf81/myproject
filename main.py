import hero
import time
import random
import combat

import numpy as np
import string

# defining Team 1
t1hero1 = hero.Adan()
t1hero2 = hero.Alma()
t1hero3 = hero.Franky()
t1hero4 = hero.Luis()

team1_hero_list = [t1hero1, t1hero2, t1hero3, t1hero4]

print(t1hero1)
team1 = {"heroM": team1_hero_list[0].name, "heroS1": t1hero2.get_name(), "heroS2": t1hero3.get_name(),
         "heroS3": t1hero4.get_name()}

#defining Enemy Team
t2hero1 = hero.Chino()
t2hero2 = hero.Gil()
t2hero3 = hero.Lalo()
t2hero4 = hero.Sherman()



team2 = {"heroM": t2hero1.get_name(), "heroS1": t2hero3.get_name(), "heroS2": t2hero4.get_name(),
         "heroS3": t2hero2.get_name()}

team1_name = "ScRuS"
team2_name = "Fire Level 1"


#function to display team information, hero position, and battling hero
def team_display():

    print(f"""

    {team1_name.center(25,"-")}                            {team2_name.center(25,"-")}
    S3. {team1["heroS3"].ljust(20)}                             S3. {team2["heroS3"].ljust(20)}  
    S2. {team1["heroS2"].ljust(20)}             VS              S2. {team2["heroS2"].ljust(20)} 
    S1. {str(team1["heroS1"]).ljust(20)}                             S1. {team2["heroS1"].ljust(20)} 
    ####################                                 ####################
    SM {team1["heroM"].ljust(20)}                               SM {team2["heroM"].center(20)} 
    """)

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




#print(hero.adan_hero["position"]["main"])


def battle():

    team_display()
    print("Round 1")
    print(f"{t1hero1.get_name()} and {t2hero1.get_name()} step in for battle")
    time.sleep(2)
    combat_stats(t1hero1, t2hero1)
    a_move = "kinto_attack"
    d_hp = combat.fight_boss(t1hero1, a_move, t1hero2, t1hero3, t1hero4, t2hero1, t2hero2, t2hero3, t2hero4)
    t2hero1.set_health(d_hp)
    time.sleep(3)

    #team_display()
    combat_stats(t1hero1, t2hero1)
    d_hp = combat.fight_hero(t2hero1, a_move, t2hero2, t2hero3, t2hero4, t1hero1, t1hero2, t1hero3, t1hero4)
    time.sleep(3)
    print("Round 2")
    combat_stats(t1hero1, t2hero1)

def main():
    battle()

main()










# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
