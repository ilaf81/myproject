# function to handles team building
import hero

# function for training

def training_menu():
    pass


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
    print("[3] Power up")
    print("[4] Build Team")
    print("[5] Go to Dungeon")
    print("[0] Exit the Game\n")


def team_build_menu():
    print(" --Team Building Menu--")
    print("[1] Edit Position 1")
    print("[2] Edit Position 2")
    print("[3] Edit Position 3")
    print("[4] Edit Position 4")
    print("[0] Exit the Game")
