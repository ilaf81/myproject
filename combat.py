# This page will create the functions to handle the combat system
import random
import time

# function to reset combat variables per round

def reset_round_var(hero, hero2, hero3, hero4):
    hero.move["chase_attack"]["used"] = False
    hero2.move["chase_attack"]["used"] = False
    hero3.move["chase_attack"]["used"] = False
    hero4.move["chase_attack"]["used"] = False


# function that handles chase attack
def chase_attack(hero, e_hero):
    hero_name = hero.get_name()
    hero_str = hero.get_strength()
    hero_int = hero.get_intellect()
    hero_ch_atk_dmg = hero.move["chase_attack"]["damage"]
    hero_ch_atk_name = hero.move["chase_attack"]["name"]
    e_h_def = e_hero.get_defense()
    chase_dmg = hero_ch_atk_dmg + (hero_str * 3) - (e_h_def * 2)
    print(
        f"{hero_name} follows with {hero_ch_atk_name}. {chase_dmg} damage...")
    return chase_dmg



def fight_boss(t1h1,a_move, t1h2, t1h3, t1h4, t2h1, t2h2, t2h3, t2h4):
    # defining all variables that can we used in combat for utilization
    # Front hero stats variables
    heroF_name = t1h1.get_name()
    heroF_hp = t1h1.stats["health points"]
    heroF_str = t1h1.get_strength()
    heroF_int = t1h1.get_intellect()
    heroF_def = t1h1.get_defense()
    heroF_mdef = t1h1.get_m_defense()
    heroF_spped = t1h1.get_speed()
    heroF_atked = t1h1.get_attacked()

    #Front Hero Spc/chase Atk variables
    heroF_SpcAtk_name = t1h1.move["kinto_attack"]["name"]
    heroF_SpcAtk_dmg = t1h1.move["kinto_attack"]["damage"]
    heroF_SpcAtk_cause = t1h1.move["kinto_attack"]["cause"]
    heroF_SpcAtk_type = t1h1.move["kinto_attack"]["type"]
    heroF_SpcAtk_cooldown = t1h1.move["kinto_attack"]["cool-down"]

    heroF_ChAtk_name = t1h1.move["chase_attack"]["name"]
    heroF_ChAtk_dmg = t1h1.move["chase_attack"]["damage"]
    heroF_ChAtk_chase = t1h1.move["chase_attack"]["chase"]
    heroF_ChAtk_cause = t1h1.move["chase_attack"]["cause"]
    heroF_ChAtk_type = t1h1.move["chase_attack"]["type"]

    heroF_supAtk_name = t1h1.move["support"]["name"]
    heroF_supAtk_pwr = t1h1.move["support"]["power"]
    heroF_supAtk_type = t1h1.move["support"]["type"]

    heroF_passive_name = t1h1.move["passive"]["name"]
    heroF_passive_action = t1h1.move["passive"]["action"]
    heroF_passive_type = t1h1.move["passive"]["type"]


    t1h1_m_attack = t1h1.move[a_move]
    t1s1_chase = t1h2.move["chase_attack"]

    t1h1_name = t1h1.get_name()
    chase_dmg = 0
    h2hp = t2h1.get_health()
    print(f"{heroF_name}'s begins")
    h2def = t2h1.get_defense()
    damage = heroF_SpcAtk_dmg + (heroF_str * 3) - int(h2def) * 2
    print(f"{heroF_name} uses {heroF_SpcAtk_name}. {damage} damage...")
    h2hp = h2hp - damage
    time.sleep(2)
    current_cause = heroF_SpcAtk_cause
    chase_active = True
    chase_counter = 0
    while chase_active:
        if current_cause == t1h1.move["chase_attack"]["chase"] and t1h1.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t1h1.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t1h1, t2h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t1h1.move["chase_attack"]["used"] = True
            current_cause = t1h1.move["chase_attack"]["cause"]


        elif current_cause == t1h2.move["chase_attack"]["chase"] and t1h2.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t1h2.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t1h2, t2h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t1h2.move["chase_attack"]["used"] = True
            current_cause = t1h2.move["chase_attack"]["cause"]


        elif current_cause == t1h3.move["chase_attack"]["chase"] and t1h3.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t1h3.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t1h3, t2h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t1h3.move["chase_attack"]["used"] = True
            current_cause = t1h3.move["chase_attack"]["cause"]

        elif current_cause == t1h4.move["chase_attack"]["chase"] and t1h4.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t1h4.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t1h4, t2h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t1h4.move["chase_attack"]["used"] = True
            current_cause = t1h4.move["chase_attack"]["cause"]
        if chase_counter >= 7:
            chase_active = False

        chase_counter += 1

    print(f"{t2h1.get_name()} now has {h2hp} hit points!")
    print("Turn Ends")
    reset_round_var(t1h1, t1h2, t1h3, t1h4)
    return h2hp


def fight_hero(t2h1, a_move, t2h2, t2h3, t2h4, t1h1, t1h2, t1h3, t1h4,):
    # defining all variables that can we used in combat for utilization
    # Front hero stats variables
    heroF_name = t2h1.get_name()
    heroF_hp = t2h1.stats["health points"]
    heroF_str = t2h1.get_strength()
    heroF_int = t2h1.get_intellect()
    heroF_def = t2h1.get_defense()
    heroF_mdef = t2h1.get_m_defense()
    heroF_spped = t2h1.get_speed()
    heroF_atked = t2h1.get_attacked()

    #Front Hero Spc/chase Atk variables
    heroF_SpcAtk_name = t2h1.move["kinto_attack"]["name"]
    heroF_SpcAtk_dmg = t2h1.move["kinto_attack"]["damage"]
    heroF_SpcAtk_cause = t2h1.move["kinto_attack"]["cause"]
    heroF_SpcAtk_type = t2h1.move["kinto_attack"]["type"]
    heroF_SpcAtk_cooldown = t2h1.move["kinto_attack"]["cool-down"]

    heroF_ChAtk_name = t2h1.move["chase_attack"]["name"]
    heroF_ChAtk_dmg = t2h1.move["chase_attack"]["damage"]
    heroF_ChAtk_chase = t2h1.move["chase_attack"]["chase"]
    heroF_ChAtk_cause = t2h1.move["chase_attack"]["cause"]
    heroF_ChAtk_type = t2h1.move["chase_attack"]["type"]

    heroF_supAtk_name = t2h1.move["support"]["name"]
    heroF_supAtk_pwr = t2h1.move["support"]["power"]
    heroF_supAtk_type = t2h1.move["support"]["type"]

    heroF_passive_name = t2h1.move["passive"]["name"]
    heroF_passive_action = t2h1.move["passive"]["action"]
    heroF_passive_type = t2h1.move["passive"]["type"]


    t1h1_m_attack = t2h1.move[a_move]
    t1s1_chase = t2h2.move["chase_attack"]

    t1h1_name = t2h1.get_name()
    chase_dmg = 0
    h2hp = t1h1.get_health()
    print(f"{heroF_name}'s begins")
    h2def = t1h1.get_defense()
    damage = heroF_SpcAtk_dmg + (heroF_str * 3) - int(h2def) * 2
    print(f"{heroF_name} uses {heroF_SpcAtk_name}. {damage} damage...")
    h2hp = h2hp - damage
    time.sleep(2)
    current_cause = heroF_SpcAtk_cause
    chase_active = True
    chase_counter = 0
    while chase_active:
        if current_cause == t2h1.move["chase_attack"]["chase"] and t2h1.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t2h1.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t2h1, t1h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t2h1.move["chase_attack"]["used"] = True
            current_cause = t2h1.move["chase_attack"]["cause"]


        elif current_cause == t2h2.move["chase_attack"]["chase"] and t2h2.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t2h2.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t2h2, t1h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t2h2.move["chase_attack"]["used"] = True
            current_cause = t1h2.move["chase_attack"]["cause"]


        elif current_cause == t2h3.move["chase_attack"]["chase"] and t2h3.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t2h3.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t2h3, t2h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t2h3.move["chase_attack"]["used"] = True
            current_cause = t1h3.move["chase_attack"]["cause"]

        elif current_cause == t2h4.move["chase_attack"]["chase"] and t2h4.move["chase_attack"]["used"] is False:
            chase_counter += 1
            cause_atk_name = t2h4.move["chase_attack"]["name"]
            # calling chase function to get chase damage
            chase_dmg = chase_attack(t2h4, t1h1)

            time.sleep(2)

            h2hp = h2hp - chase_dmg

            t2h4.move["chase_attack"]["used"] = True
            current_cause = t2h4.move["chase_attack"]["cause"]
        if chase_counter >= 7:
            chase_active = False

        chase_counter += 1

    print(f"{t1h1.get_name()} now has {h2hp} hit points!")
    print("Turn Ends")
    reset_round_var(t1h1, t1h2, t1h3, t1h4)
    return h2hp

