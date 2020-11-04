import hero
import time
import numpy as np
import string

team1 = {"heroM": hero.adan_hero["name"], "heroS1": hero.alma_hero["name"], "heroS2": hero.franky_hero["name"],
         "heroS3": hero.luis_hero["name"]}

team2 = {"heroM": hero.gil_hero["name"], "heroS1": hero.lalo_hero["name"], "heroS2": hero.sherman_hero["name"],
         "heroS3": hero.chino_hero["name"]}
team1_name = "ScRuS"
team2_name = "TLC"

print(team1)
print(f"""

{team1_name.center(25,"-")}                            {team2_name.center(25,"-")}
S3. {team2["heroS3"].ljust(20)}                             S3. {team1["heroS3"].ljust(20)}  
S2. {team2["heroS2"].ljust(20)}             VS              S2. {team1["heroS2"].ljust(20)} 
S1. {str(team2["heroS1"]).ljust(20)}                             S1. {team1["heroS1"].ljust(20)} 
####################                                 ####################
SM {team2["heroM"].ljust(20)}                               SM {team1["heroM"].center(20)} 
""")
#print(hero.adan_hero["position"]["main"])


def battle():

    pass







# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
