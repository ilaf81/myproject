import hero
import time
import random

import numpy as np
import string

# defining Team 1
t1hero1 = hero.Adan()
t1hero2 = hero.Alma()
t1hero3 = hero.Franky()
t1hero4 = hero.Luis()


print(t1hero1)
team1 = {"heroM": t1hero1.name, "heroS1": t1hero2.get_name(), "heroS2": t1hero3.get_name(),
         "heroS3": t1hero4.get_name()}

#defining Enemy Team
t2hero1 = hero.Chino()
t2hero2 = hero.Gil()
t2hero3 = hero.Lalo()
t2hero4 = hero.Sherman()

team2 = {"heroM": t2hero2.get_name(), "heroS1": t2hero3.get_name(), "heroS2": t2hero4.get_name(),
         "heroS3": t2hero1.get_name()}

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
    hp1 = str(hero_s.stats["health points"])
    def1 = str(hero_s.stats["defense"])
    str1 = str(hero_s.stats["strength"])
    int1 = str(hero_s.stats["intellect"])
    spd1 = str(hero_s.stats["speed"])
    ele1 = hero_s.element
    #hero 2 stats
    name2 = hero_s2.name
    hp2 = str(hero_s2.stats["health points"])
    def2 = str(hero_s2.stats["defense"])
    str2 = str(hero_s2.stats["strength"])
    int2 = str(hero_s2.stats["intellect"])
    spd2 = str(hero_s2.stats["speed"])
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


def fight(hero1, hero2):

    h1atk = hero1.stats["strength"]
    h2def = hero2.stats["defense"]
    m_atk = hero1.move["kinto_attack"]["damage"]
    damage = int(m_atk) + (int(h1atk) * 3 - int(h2def) * 2)
    h2hp = hero2.stats["health points"]
    h2hp = int(h2hp) - damage
    #hero2["health points"] = int(damage)
    return h2hp

#print(hero.adan_hero["position"]["main"])


def battle():
    print("Round 1")
    team_display()
    combat_stats(t1hero1, t2hero2)
    d_hp = fight(t1hero1, t2hero2)
    t2hero2.stats["health points"] = d_hp
    time.sleep(3)
    print("Round 2")
    team_display()
    combat_stats(t1hero1, t2hero2)
    time.sleep(3)
    print("Round 3")

def main():
    battle()

main()










# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
