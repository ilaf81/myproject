# This page will create the functions to handle the combat system
import random
import time

def fight(t1h1,a_move, t1h2, t1h3, t1h4, t2h1, t2h2, t2h3, t2h4):



    t1h1_m_attack = t1h1.move["kinto_attack"]
    t1s1_chase = t1h2.move["chase_attack"]
    chase_dmg = 0
    print("BATTLE BEGINS")
    h1atk = t1h1.get_strength()
    h2def = t2h1.get_defense()
    main_atk = t1h1.move[a_move]["damage"]
    damage = int(main_atk) + (int(h1atk) * 3 - int(h2def) * 2)
    print(f"{t1h1.get_name()} uses {t1h1.move[a_move]['name']}. {damage} damage...")
    time.sleep(2)
    if t1h1_m_attack["cause"] == t1s1_chase["chase"]:

        chase_dmg = int(t1s1_chase["damage"]) + (int(t1h2.get_strength()) * 3) - (int(h2def) * 2)
        print(f"{t1h2.get_name()} follows {t1h1.get_name()}'s {t1h1.move[a_move]['name']} with {t1s1_chase['name']}. {chase_dmg} damage...")
        time.sleep(2)
        h2hp = t2h1.get_health()

        h2hp = int(h2hp) - damage - chase_dmg
        print(f"{t2h1.get_name()} now has {h2hp} hit points!")
        return h2hp

