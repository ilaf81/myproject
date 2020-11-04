import hero
import time
import numpy as np
import string

# defining Team 1
t1hero1 = hero.luis_hero

team1 = {"heroM": hero.adan_hero["name"], "heroS1": hero.alma_hero["name"], "heroS2": hero.franky_hero["name"],
         "heroS3": hero.luis_hero["name"]}

#defining Enemy Team
t2hero1 = hero.chino_hero

team2 = {"heroM": hero.gil_hero["name"], "heroS1": hero.lalo_hero["name"], "heroS2": hero.sherman_hero["name"],
         "heroS3": hero.chino_hero["name"]}

team1_name = "ScRuS"
team2_name = "Fire Level 1"


#function to display team information, hero position, and battling hero
def team_display():

    print(f"""

    {team1_name.center(25,"-")}                            {team2_name.center(25,"-")}
    S3. {team2["heroS3"].ljust(20)}                             S3. {team1["heroS3"].ljust(20)}  
    S2. {team2["heroS2"].ljust(20)}             VS              S2. {team1["heroS2"].ljust(20)} 
    S1. {str(team2["heroS1"]).ljust(20)}                             S1. {team1["heroS1"].ljust(20)} 
    ####################                                 ####################
    SM {team2["heroM"].ljust(20)}                               SM {team1["heroM"].center(20)} 
    """)

def combat_stats(hero_s, hero_s2):
    #hero 1 stats
    name1 = hero_s["name"]
    hp1 = str(hero_s["health points"])
    def1 = str(hero_s["defense"])
    str1 = str(hero_s["strength"])
    int1 = str(hero_s["intellect"])
    spd1 = str(hero_s["speed"])
    ele1 = hero_s["element"]
    #hero 2 stats
    name2 = hero_s2["name"]
    hp2 = str(hero_s2["health points"])
    def2 = str(hero_s2["defense"])
    str2 = str(hero_s2["strength"])
    int2 = str(hero_s2["intellect"])
    spd2 = str(hero_s2["speed"])
    ele2 = hero_s2["element"]
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

    h1atk = hero1["strength"]
    h2def = hero2["defense"]
    m_atk = hero1["moves"]["kinto_attack"]["damage"]
    damage = int(m_atk) + (int(h1atk) * 4 - int(h2def) * 2)
    h2hp = hero2["health points"]
    h2hp = int(h2hp) - damage
    #hero2["health points"] = int(damage)
    return h2hp

#print(hero.adan_hero["position"]["main"])


def battle():
    print("Round 1")
    team_display()
    combat_stats(t1hero1, t2hero1)
    d_hp = fight(t1hero1, t2hero1)
    t2hero1["health points"] = d_hp
    time.sleep(3)
    print("Round 2")
    team_display()
    combat_stats(t1hero1, t2hero1)
    time.sleep(3)
    print("Round 3")

def main():
    battle()

main()










# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
