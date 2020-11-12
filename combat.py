# This page will create the functions to handle the combat system
import random
import time


# creating battle menu
def battle_menu():
    print(" --Battle Menu--")
    print("[1] Inventory")
    print("[2] Show Teams")
    print("[3] Use Kinto Attack")
    print("[4] Use Standard Attack")
    print("[5] End round")
    print("[0] Retreat\n")

# healing function

def healling(int, power):
    heals = int + power
    return heals

# type damage function
def type_damage( damage, type_dmg, str , int):
    if type_dmg == "str":
        t_damage = damage + (str * 3)
    elif type_dmg == "int":
        t_damage = damage + (int * 3)
    else:
        t_damage = damage + (((int/2) + (str/2)) * 3)
    return t_damage

def element_msg_bonus(h_element, e_element):
    messege_element_bonus = ""
    if h_element == e_element:
        messege_element_bonus = "but it's not very effective"

    elif h_element == "Fire" and e_element == "Wind":
        messege_element_bonus = "and it's very effective"

    elif h_element == "Fire" and e_element == "Water":
        messege_element_bonus = "but it's very weak"

    elif h_element == "Wind" and e_element == "Lighting":
        messege_element_bonus = "and it's very effective"

    elif h_element == "Wind" and e_element == "Fire":
        messege_element_bonus = "but it's very weak"

    elif h_element == "Lighting" and e_element == "Earth":
        messege_element_bonus = "and it's very effective"

    elif h_element == "Lighting" and e_element == "Wind":
        messege_element_bonus = "but it's very weak"

    elif h_element == "Earth" and e_element == "Water":
        messege_element_bonus = "and it's very effective"

    elif h_element == "Earth" and e_element == "Lighting":
        messege_element_bonus = "but it's very weak"

    elif h_element == "Water" and e_element == "Fire":
        messege_element_bonus = "and it's very effective"

    elif h_element == "Water" and e_element == "Earth":
        messege_element_bonus = "but it's very weak"
    else:
        messege_element_bonus = ""

    return messege_element_bonus

# element bonus damage function
def element_bonus( damage , h_element, e_element):
    if h_element == e_element:

        damage = damage * 0.90
        time.sleep(1)
    elif h_element == "Fire" and e_element == "Wind":

        damage = damage * 1.35
        time.sleep(1)
    elif h_element == "Fire" and e_element == "Water":

        damage = damage * 0.65
        time.sleep(1)
    elif h_element == "Wind" and e_element == "Lighting":

        damage = damage * 1.35
        time.sleep(1)
    elif h_element == "Wind" and e_element == "Fire":

        damage = damage * 0.65
        time.sleep(1)
    elif h_element == "Lighting" and e_element == "Earth":

        damage = damage * 1.35
        time.sleep(1)
    elif h_element == "Lighting" and e_element == "Wind":

        damage = damage * 0.65
        time.sleep(1)
    elif h_element == "Earth" and e_element == "Water":

        damage = damage * 1.35
        time.sleep(1)
    elif h_element == "Earth" and e_element == "Lighting":

        damage = damage * 0.65
        time.sleep(1)
    elif h_element == "Water" and e_element == "Fire":

        damage = damage * 1.35
        time.sleep(1)
    elif h_element == "Water" and e_element == "Earth":

        damage = damage * 0.65
        time.sleep(1)
    return damage


# standard attack function
def standard_attack(hero1, hero2, hero3, hero4, e_boss, teams_name):
    hero_list = [hero1, hero2, hero3, hero4]
    enemy_main = e_boss
    print(f"{teams_name} gets ready for battle")
    for team_member in hero_list:
        tm_main_name = team_member.get_name()
        tm_main_str = team_member.get_strength()
        tm_main_int = team_member.get_strength()
        tm_main_element = team_member.get_element()

        tm_main_StdAtk_name = team_member.move["standard_attack"]["name"]
        tm_main_StdAtk_damge = team_member.move["standard_attack"]["power"]
        tm_main_StdAtk_cause = team_member.move["standard_attack"]["cause"]
        tm_main_StdAtk_type = team_member.move["standard_attack"]["type"]
        tm_main_StdAtk_heals = team_member.move["standard_attack"]["heals"]

        if tm_main_StdAtk_heals == True:
           heroM_name = hero1.get_name()
           pwr_heal = healling(tm_main_int, tm_main_StdAtk_damge)
           heroM_hp = hero1.get_health() + pwr_heal
           hero1.set_health(heroM_hp)
           current_cause = tm_main_StdAtk_cause
           print(f"{tm_main_name} uses {tm_main_StdAtk_name}")
           print(f"heals {pwr_heal} to {heroM_name} and {current_cause} ")
           time.sleep(2)
        else:
            pwr_damage = type_damage(tm_main_StdAtk_damge, tm_main_StdAtk_type, tm_main_str, tm_main_int)
            enemy_health = enemy_main.get_health()
            enemy_element = enemy_main.get_element()

            current_cause = tm_main_StdAtk_cause
            h1def = enemy_main.get_defense()
            damage = tm_main_StdAtk_damge + pwr_damage - int(h1def) * 3
            damage = element_bonus(damage, tm_main_element, enemy_element)
            damage = round(damage, 2)
            msg_element = element_msg_bonus(tm_main_element, enemy_element)
            print(f"{tm_main_name} uses {tm_main_StdAtk_name}")
            print(f"causing {damage} {tm_main_element} damage and {current_cause} {msg_element} ")
            enemy_health = enemy_health - damage
            time.sleep(2)
            current_cause = tm_main_StdAtk_cause

        chase_active = True
        chase_counter = 0
        while chase_active:
            if current_cause == hero1.move["chase_attack"]["chase"] and hero1.move["chase_attack"]["used"] is False:
                chase_counter += 1
                h_element = hero1.get_element()
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero1, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero1.move["chase_attack"]["used"] = True
                current_cause = hero1.move["chase_attack"]["cause"]


            elif current_cause == hero2.move["chase_attack"]["chase"] and hero2.move["chase_attack"]["used"] is False:
                chase_counter += 1
                h_element = hero2.get_element()
                cause_atk_name = hero2.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero2, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero2.move["chase_attack"]["used"] = True
                current_cause = hero2.move["chase_attack"]["cause"]


            elif current_cause == hero3.move["chase_attack"]["chase"] and hero3.move["chase_attack"]["used"] is False:
                chase_counter += 1

                cause_atk_name = hero3.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero3, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero3.move["chase_attack"]["used"] = True
                current_cause = hero3.move["chase_attack"]["cause"]

            elif current_cause == hero4.move["chase_attack"]["chase"] and hero4.move["chase_attack"]["used"] is False:
                chase_counter += 1
                cause_atk_name = hero4.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero4, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero4.move["chase_attack"]["used"] = True
                current_cause = hero4.move["chase_attack"]["cause"]
            if chase_counter >= 7:
                chase_active = False

            chase_counter += 1
        if tm_main_StdAtk_heals == False:
            enemy_main.set_health(enemy_health)



    print(f"{enemy_main.get_name()} now has {enemy_health} hit points!")
    print("Standard Attacks End")
    return enemy_health
# function to reset combat variables per round

def reset_round_var(hero, hero2, hero3, hero4):
    hero.move["chase_attack"]["used"] = False
    hero2.move["chase_attack"]["used"] = False
    hero3.move["chase_attack"]["used"] = False
    hero4.move["chase_attack"]["used"] = False


# function that handles chase attack
def chase_attack(hero, e_hero, pre_cause):
    hero_name = hero.get_name()
    hero_str = hero.get_strength()
    hero_element = hero.get_element()
    hero_int = hero.get_intellect()
    hero_ch_atk_dmg = hero.move["chase_attack"]["damage"]
    hero_ch_atk_name = hero.move["chase_attack"]["name"]
    hero_ch_atk_cause = hero.move["chase_attack"]["cause"]
    e_h_def = e_hero.get_defense()
    enemy_element = e_hero.get_element()

    chase_dmg = hero_ch_atk_dmg + (hero_str * 3) - (e_h_def * 3)
    chase_dmg = element_bonus(chase_dmg, hero_element, enemy_element)
    msg_element = element_msg_bonus(hero_element, enemy_element)
    print(f"{hero_name} chase the {pre_cause} with {hero_ch_atk_name}")
    chase_dmg = round(chase_dmg, 2)
    print(f"causing {chase_dmg} {hero_element} damage and {hero_ch_atk_cause} {msg_element}")
    return chase_dmg



def kinto_attack(hero1, hero2, hero3, hero4, e_boss, team_name):
    hero_list = [hero1]
    enemy_main = e_boss
    print(f"{team_name} gets ready for battle")
    for team_member in hero_list:
        tm_main_name = team_member.get_name()
        tm_main_str = team_member.get_strength()
        tm_main_int = team_member.get_strength()
        tm_main_element = team_member.get_element()

        tm_main_KintodAtk_name = team_member.move["kinto_attack"]["name"]
        tm_main_KintoAtk_damge = team_member.move["kinto_attack"]["damage"]
        tm_main_KintoAtk_cause = team_member.move["kinto_attack"]["cause"]
        tm_main_KintoAtk_type = team_member.move["kinto_attack"]["type"]
        tm_main_KintoAtk_heals = team_member.move["kinto_attack"]["heals"]

        if tm_main_KintoAtk_heals == True:
           heroM_name = hero1.get_name()
           pwr_heal = healling(tm_main_int, tm_main_KintoAtk_damge)
           heroM_hp = hero1.get_health() + pwr_heal
           hero1.set_health(heroM_hp)
           current_cause = tm_main_KintoAtk_cause
           print(f"{tm_main_name} uses {tm_main_KintodAtk_name}")
           print(f"heals {pwr_heal} to {heroM_name} and {current_cause} ")
           time.sleep(2)
        else:
            pwr_damage = type_damage(tm_main_KintoAtk_damge, tm_main_KintoAtk_type, tm_main_str, tm_main_int)
            enemy_health = enemy_main.get_health()
            enemy_element = enemy_main.get_element()

            current_cause = tm_main_KintoAtk_cause
            h1def = enemy_main.get_defense()
            damage = pwr_damage - int(h1def) * 3
            damage = element_bonus(damage, tm_main_element, enemy_element)
            msg_element = element_msg_bonus(tm_main_element, enemy_element)
            print(f"{tm_main_name} uses {tm_main_KintodAtk_name}")
            print(f"causing {damage} {tm_main_element} damage and {current_cause} {msg_element} ")
            enemy_health = enemy_health - damage
            time.sleep(2)
            current_cause = tm_main_KintoAtk_cause

        chase_active = True
        chase_counter = 0
        while chase_active:
            if current_cause == hero1.move["chase_attack"]["chase"] and hero1.move["chase_attack"]["used"] is False:
                chase_counter += 1
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero1, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero1.move["chase_attack"]["used"] = True
                current_cause = hero1.move["chase_attack"]["cause"]


            elif current_cause == hero2.move["chase_attack"]["chase"] and hero2.move["chase_attack"]["used"] is False:
                chase_counter += 1
                cause_atk_name = hero2.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero2, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero2.move["chase_attack"]["used"] = True
                current_cause = hero2.move["chase_attack"]["cause"]


            elif current_cause == hero3.move["chase_attack"]["chase"] and hero3.move["chase_attack"]["used"] is False:
                chase_counter += 1
                cause_atk_name = hero3.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero3, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero3.move["chase_attack"]["used"] = True
                current_cause = hero3.move["chase_attack"]["cause"]

            elif current_cause == hero4.move["chase_attack"]["chase"] and hero4.move["chase_attack"]["used"] is False:
                chase_counter += 1
                cause_atk_name = hero4.move["chase_attack"]["name"]
                # calling chase function to get chase damage
                chase_dmg = chase_attack(hero4, enemy_main, current_cause)

                time.sleep(2)

                enemy_health = enemy_health - chase_dmg

                hero4.move["chase_attack"]["used"] = True
                current_cause = hero4.move["chase_attack"]["cause"]
            if chase_counter >= 7:
                chase_active = False

            chase_counter += 1

        enemy_main.set_health(enemy_health)

    enemy_health = round(enemy_health, 2)
    print(f"{enemy_main.get_name()} now has {enemy_health} hit points!")
    print("Kinto Attack End")

    return enemy_health

def kinto_attack_slected(hero1, hero2, hero3, hero4, e_boss):

    enemy_main = e_boss

    tm_main_name = hero1.get_name()
    tm_main_str = hero1.get_strength()
    tm_main_int = hero1.get_strength()
    tm_main_element = hero1.get_element()

    tm_main_KintodAtk_name = hero1.move["kinto_attack"]["name"]
    tm_main_KintoAtk_damge = hero1.move["kinto_attack"]["damage"]
    tm_main_KintoAtk_cause = hero1.move["kinto_attack"]["cause"]
    tm_main_KintoAtk_type = hero1.move["kinto_attack"]["type"]
    tm_main_KintoAtk_heals = hero1.move["kinto_attack"]["heals"]

    print(f"{tm_main_name} gets ready for battle")
    if tm_main_KintoAtk_heals == True:
        heroM_name = hero1.get_name()
        pwr_heal = healling(tm_main_int, tm_main_KintoAtk_damge)
        heroM_hp = hero1.get_health() + pwr_heal
        hero1.set_health(heroM_hp)
        current_cause = tm_main_KintoAtk_cause
        print(f"{tm_main_name} uses {tm_main_KintodAtk_name}")
        print(f"heals {pwr_heal} to {heroM_name} and {current_cause} ")
        time.sleep(2)
    else:
        pwr_damage = type_damage(tm_main_KintoAtk_damge, tm_main_KintoAtk_type, tm_main_str, tm_main_int)
        enemy_health = enemy_main.get_health()
        enemy_element = enemy_main.get_element()

        current_cause = tm_main_KintoAtk_cause
        h1def = enemy_main.get_defense()
        damage = pwr_damage - int(h1def) * 3
        damage = element_bonus(damage, tm_main_element, enemy_element)
        msg_element = element_msg_bonus(tm_main_element, enemy_element)
        print(f"{tm_main_name} uses {tm_main_KintodAtk_name}")
        print(f"causing {damage} {tm_main_element} damage and {current_cause} {msg_element} ")
        enemy_health = enemy_health - damage
        time.sleep(2)
        current_cause = tm_main_KintoAtk_cause

    chase_active = True
    chase_counter = 0
    while chase_active:
        if current_cause == hero1.move["chase_attack"]["chase"] and hero1.move["chase_attack"]["used"] is False:
            chase_counter += 1
            # calling chase function to get chase damage
            chase_dmg = chase_attack(hero1, enemy_main, current_cause)

            time.sleep(2)

            enemy_health = enemy_health - chase_dmg

            hero1.move["chase_attack"]["used"] = True
            current_cause = hero1.move["chase_attack"]["cause"]


        elif current_cause == hero2.move["chase_attack"]["chase"] and hero2.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = hero2.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(hero2, enemy_main, current_cause)

            time.sleep(2)

            enemy_health = enemy_health - chase_dmg

            hero2.move["chase_attack"]["used"] = True
            current_cause = hero2.move["chase_attack"]["cause"]


        elif current_cause == hero3.move["chase_attack"]["chase"] and hero3.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = hero3.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(hero3, enemy_main, current_cause)

            time.sleep(2)

            enemy_health = enemy_health - chase_dmg

            hero3.move["chase_attack"]["used"] = True
            current_cause = hero3.move["chase_attack"]["cause"]

        elif current_cause == hero4.move["chase_attack"]["chase"] and hero4.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = hero4.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(hero4, enemy_main, current_cause)

            time.sleep(2)

            enemy_health = enemy_health - chase_dmg

            hero4.move["chase_attack"]["used"] = True
            current_cause = hero4.move["chase_attack"]["cause"]
        if chase_counter >= 7:
            chase_active = False

        chase_counter += 1

    enemy_main.set_health(enemy_health)

    enemy_health = round(enemy_health, 2)
    print(f"{enemy_main.get_name()} now has {enemy_health} hit points!")
    print("Kinto Attack End")

    return enemy_health

