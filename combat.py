# This page will create the functions to handle the combat system
import random
import time

# Main attack function




# standard attack function
def standard_attack(hero1, hero2, hero3, hero4, e_boss, teams_name):
    hero_list = [hero1, hero2, hero3, hero4]
    enemy_main = e_boss
    print(f"{teams_name} gets ready for battle")
    for team_member in hero_list:
        tm_main_name = team_member.get_name()
        tm_main_str = team_member.get_strength()
        tm_main_StdAtk_name = team_member.move["standard_attack"]["name"]
        tm_main_StdAtk_damge = team_member.move["standard_attack"]["power"]
        tm_main_StdAtk_cause = team_member.move["standard_attack"]["cause"]

        enemy_health = enemy_main.get_health()
        current_cause = tm_main_StdAtk_cause
        h1def = enemy_main.get_defense()
        damage = tm_main_StdAtk_damge + (tm_main_str * 3) - int(h1def) * 3
        print(f"{tm_main_name} uses {tm_main_StdAtk_name}. {damage} damage causing {current_cause}")
        enemy_health = enemy_health - damage
        time.sleep(2)

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

    hero_int = hero.get_intellect()
    hero_ch_atk_dmg = hero.move["chase_attack"]["damage"]
    hero_ch_atk_name = hero.move["chase_attack"]["name"]
    hero_ch_atk_cause = hero.move["chase_attack"]["cause"]
    e_h_def = e_hero.get_defense()

    chase_dmg = hero_ch_atk_dmg + (hero_str * 3) - (e_h_def * 3)
    print(
        f"{hero_name} follows {pre_cause} with {hero_ch_atk_name}. {chase_dmg} damage causing {hero_ch_atk_cause}")
    return chase_dmg



def kinto_attack(hero1, hero2, hero3, hero4, e_boss, team_name):
    hero_list = [hero1]
    enemy_main = e_boss
    print(f"{team_name} gets ready for battle")
    for team_member in hero_list:
        tm_main_name = team_member.get_name()
        tm_main_str = team_member.get_strength()
        tm_main_KintodAtk_name = team_member.move["kinto_attack"]["name"]
        tm_main_KintoAtk_damge = team_member.move["kinto_attack"]["damage"]
        tm_main_KintoAtk_cause = team_member.move["kinto_attack"]["cause"]

        enemy_health = enemy_main.get_health()
        current_cause = tm_main_KintoAtk_cause
        h1def = enemy_main.get_defense()
        damage = tm_main_KintoAtk_damge + (tm_main_str * 3) - int(h1def) * 3
        print(f"{tm_main_name} uses {tm_main_KintodAtk_name}. {damage} damage causing {current_cause}")
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



    print(f"{enemy_main.get_name()} now has {enemy_health} hit points!")
    print("Kinto Attack End")
    return enemy_health

def fight_hero(t2h1, a_move, t2h2, t2h3, t2h4, t1h1):
    # defining all variables that can we used in combat for utilization
    # Front hero stats variables
    e_health = t1h1.get_health()
    e_health = standard_attack(t2h1, t2h2, t2h3, t2h4, t1h1)

    reset_round_var(t2h1, t2h2, t2h3, t2h4)
    return e_health

