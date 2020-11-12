import hero
import time
import random
import combat
import team
import os


team_access = []




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

training_points_int = 0
training_points_str = 0
training_points_speed = 0
player_stamina = 200
player_gold = 0
player_artifacts = 1
candy_hp = 0
candy_def = 0
candy_m_def = 0
rare_candy = 0

team1_name = ""

pos1 = hero.P1()
pos2 = hero.P2()
pos3 = hero.P3()
pos4 = hero.P4()
team1_name = ""
team.welcome_message()
team.Game_Menu()


option_menu = int(input(" Enter your option >"))

while option_menu != 0:
    if option_menu == 1:
        team.training_menu()
        opt_menu_training = int(input(" Enter your option >"))
        while opt_menu_training != 0:
            if opt_menu_training == 1:
                print(f"You have {training_points_str} strength points")
                training_points_str = team.strength_training(training_points_str)
                player_stamina += 1
                print("Good Training. You stamina increased by 1")
            elif opt_menu_training == 2:
                print(f"You have {training_points_int} intellect points")
                training_points_int = team.intellect_training(training_points_int)
                player_stamina += 1
                print("Good Training. You stamina increased by 1")
            elif opt_menu_training == 3:
                print(f"You have {training_points_speed} speed points")
                training_points_speed = team.speed_training(training_points_speed)
                player_stamina += 1
                print("Good Training. You stamina increased by 1")
            elif opt_menu_training == 4:
                found_artifacts = 0
                tp_to_spend = team.quest_training(player_stamina)
                if tp_to_spend == -1:
                    player_stamina = player_stamina
                else:
                    player_stamina -= 10
                    found_artifacts = random.randint(1, 100)
                if tp_to_spend > 1:
                    player_gold += 5
                    print(f"You earned 5 gold and now have {player_gold} gold")
                    while True:
                        print(f"You have {tp_to_spend} quest points. What would you like to turn into (str/int/speed)")
                        answer_tp = input().lower().strip()
                        if answer_tp == "str":
                            training_points_str += tp_to_spend
                            print(f"Now you have {training_points_str} strength training points")
                            break
                        elif answer_tp == "int":
                            training_points_int += tp_to_spend
                            print(f"Now you have {training_points_int} intellect training points")
                            break
                        elif answer_tp == "speed":
                            training_points_speed += tp_to_spend
                            print(f"Now you have {training_points_speed} speed training points")
                            break
                        else:
                            print("Wrong input.Please try again")
                print(found_artifacts)
                if found_artifacts >= 1 and found_artifacts <= 7:
                    print("You found an artifact")
                    player_artifacts += 1
                print("Questing completed. Comeback again")

            elif opt_menu_training == 5:
                team.spend_TP_menu()
                opt_menu_spend_training = int(input(" Enter your option >"))
                while opt_menu_spend_training != 0:
                    if opt_menu_spend_training == 1:
                        team.spend_P1()
                        opt_menu_spend_P1 = int(input(" Enter your option >"))
                        while opt_menu_spend_P1 != 0:
                            if opt_menu_spend_P1 == 1:
                                print(f"You have {training_points_str} strength points")
                                print("how many would you like to use: ")
                                use_str_point = int(input())
                                if use_str_point >= training_points_str:
                                    use_str_point = training_points_str
                                    current_point = pos1.get_strength()
                                    new_str = current_point + use_str_point
                                    pos1.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                elif use_str_point > 0 and use_str_point < training_points_str:
                                    current_point = pos1.get_strength()
                                    new_str = current_point + use_str_point
                                    pos1.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 2:
                                print(f"You have {training_points_int} intellect points")
                                print("how many would you like to use: ")
                                use_int_point = int(input())
                                if use_int_point >= training_points_int:
                                    use_int_point = training_points_int
                                    current_point = pos1.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos1.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                elif use_int_point > 0 and use_int_point < training_points_int:
                                    current_point = pos1.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos1.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 3:
                                print(f"You have {training_points_speed} speed points")
                                print("how many would you like to use: ")
                                use_speed_point = int(input())
                                if use_speed_point >= training_points_speed:
                                    use_speed_point = training_points_speed
                                    current_point = pos1.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos1.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                elif use_speed_point > 0 and use_speed_point < training_points_speed:
                                    current_point = pos1.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos1.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 4:
                                print(f"You have {candy_hp} HP Candy")
                                print("how many would you like to use: ")
                                use_hp_point = int(input())
                                if use_hp_point >= candy_hp:
                                    use_hp_point = candy_hp
                                    current_point = pos1.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos1.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                elif use_hp_point > 0 and use_hp_point < candy_hp:
                                    current_point = pos1.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos1.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 5:
                                print(f"You have {candy_def} Defense Candy")
                                print("how many would you like to use: ")
                                use_def_point = int(input())
                                if use_def_point >= candy_def:
                                    use_def_point = candy_def
                                    current_point = pos1.get_defense()
                                    new_def = current_point + use_def_point
                                    pos1.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                elif use_def_point > 0 and use_def_point < candy_def:
                                    current_point = pos1.get_defense()
                                    new_def = current_point + use_def_point
                                    pos1.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 6:
                                print(f"You have {candy_m_def} M Defense Candy")
                                print("how many would you like to use: ")
                                use_m_def_point = int(input())
                                if use_m_def_point >= candy_m_def:
                                    use_m_def_point = candy_m_def
                                    current_point = pos1.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos1.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                elif use_m_def_point > 0 and use_m_def_point < candy_m_def:
                                    current_point = pos1.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos1.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P1 == 7:
                                hero.position_data(pos1)
                            else:
                                print("Invalid option")
                            team.spend_P1()
                            opt_menu_spend_P1 = int(input(" Enter your option >"))

                    elif opt_menu_spend_training == 2:
                        team.spend_P2()
                        opt_menu_spend_P2 = int(input(" Enter your option >"))
                        while opt_menu_spend_P2 != 0:
                            if opt_menu_spend_P2 == 1:
                                print(f"You have {training_points_str} strength points")
                                print("how many would you like to use: ")
                                use_str_point = int(input())
                                if use_str_point >= training_points_str:
                                    use_str_point = training_points_str
                                    current_point = pos2.get_strength()
                                    new_str = current_point + use_str_point
                                    pos2.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                elif use_str_point > 0 and use_str_point < training_points_str:
                                    current_point = pos2.get_strength()
                                    new_str = current_point + use_str_point
                                    pos2.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 2:
                                print(f"You have {training_points_int} intellect points")
                                print("how many would you like to use: ")
                                use_int_point = int(input())
                                if use_int_point >= training_points_int:
                                    use_int_point = training_points_int
                                    current_point = pos2.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos2.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                elif use_int_point > 0 and use_int_point < training_points_int:
                                    current_point = pos2.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos2.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 3:
                                print(f"You have {training_points_speed} speed points")
                                print("how many would you like to use: ")
                                use_speed_point = int(input())
                                if use_speed_point >= training_points_speed:
                                    use_speed_point = training_points_speed
                                    current_point = pos2.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos2.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                elif use_speed_point > 0 and use_speed_point < training_points_speed:
                                    current_point = pos2.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos2.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 4:
                                print(f"You have {candy_hp} HP Candy")
                                print("how many would you like to use: ")
                                use_hp_point = int(input())
                                if use_hp_point >= candy_hp:
                                    use_hp_point = candy_hp
                                    current_point = pos2.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos2.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                elif use_hp_point > 0 and use_hp_point < candy_hp:
                                    current_point = pos2.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos2.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 5:
                                print(f"You have {candy_def} Defense Candy")
                                print("how many would you like to use: ")
                                use_def_point = int(input())
                                if use_def_point >= candy_def:
                                    use_def_point = candy_def
                                    current_point = pos2.get_defense()
                                    new_def = current_point + use_def_point
                                    pos2.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                elif use_def_point > 0 and use_def_point < candy_def:
                                    current_point = pos2.get_defense()
                                    new_def = current_point + use_def_point
                                    pos2.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 6:
                                print(f"You have {candy_m_def} M Defense Candy")
                                print("how many would you like to use: ")
                                use_m_def_point = int(input())
                                if use_m_def_point >= candy_m_def:
                                    use_m_def_point = candy_m_def
                                    current_point = pos2.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos2.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                elif use_m_def_point > 0 and use_m_def_point < candy_m_def:
                                    current_point = pos2.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos2.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P2 == 7:
                                hero.position_data(pos2)
                            else:
                                print("Invalid option")
                            team.spend_P2()
                            opt_menu_spend_P2 = int(input(" Enter your option >"))
                    elif opt_menu_spend_training == 3:
                        team.spend_P3()
                        opt_menu_spend_P3 = int(input(" Enter your option >"))
                        while opt_menu_spend_P3 != 0:
                            if opt_menu_spend_P3 == 1:
                                print(f"You have {training_points_str} strength points")
                                print("how many would you like to use: ")
                                use_str_point = int(input())
                                if use_str_point >= training_points_str:
                                    use_str_point = training_points_str
                                    current_point = pos3.get_strength()
                                    new_str = current_point + use_str_point
                                    pos3.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                elif use_str_point > 0 and use_str_point < training_points_str:
                                    current_point = pos3.get_strength()
                                    new_str = current_point + use_str_point
                                    pos3.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 2:
                                print(f"You have {training_points_int} intellect points")
                                print("how many would you like to use: ")
                                use_int_point = int(input())
                                if use_int_point >= training_points_int:
                                    use_int_point = training_points_int
                                    current_point = pos3.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos3.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                elif use_int_point > 0 and use_int_point < training_points_int:
                                    current_point = pos3.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos3.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 3:
                                print(f"You have {training_points_speed} speed points")
                                print("how many would you like to use: ")
                                use_speed_point = int(input())
                                if use_speed_point >= training_points_speed:
                                    use_speed_point = training_points_speed
                                    current_point = pos3.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos3.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                elif use_speed_point > 0 and use_speed_point < training_points_speed:
                                    current_point = pos3.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos3.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 4:
                                print(f"You have {candy_hp} HP Candy")
                                print("how many would you like to use: ")
                                use_hp_point = int(input())
                                if use_hp_point >= candy_hp:
                                    use_hp_point = candy_hp
                                    current_point = pos3.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos3.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                elif use_hp_point > 0 and use_hp_point < candy_hp:
                                    current_point = pos3.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos3.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 5:
                                print(f"You have {candy_def} Defense Candy")
                                print("how many would you like to use: ")
                                use_def_point = int(input())
                                if use_def_point >= candy_def:
                                    use_def_point = candy_def
                                    current_point = pos3.get_defense()
                                    new_def = current_point + use_def_point
                                    pos3.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                elif use_def_point > 0 and use_def_point < candy_def:
                                    current_point = pos3.get_defense()
                                    new_def = current_point + use_def_point
                                    pos3.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 6:
                                print(f"You have {candy_m_def} M Defense Candy")
                                print("how many would you like to use: ")
                                use_m_def_point = int(input())
                                if use_m_def_point >= candy_m_def:
                                    use_m_def_point = candy_m_def
                                    current_point = pos3.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos3.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                elif use_m_def_point > 0 and use_m_def_point < candy_m_def:
                                    current_point = pos3.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos3.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P3 == 7:
                                hero.position_data(pos3)
                            else:
                                print("Invalid option")
                            team.spend_P3()
                            opt_menu_spend_P3 = int(input(" Enter your option >"))
                    elif opt_menu_spend_training == 4:
                        team.spend_P4()
                        opt_menu_spend_P4 = int(input(" Enter your option >"))
                        while opt_menu_spend_P4 != 0:
                            if opt_menu_spend_P4 == 1:
                                print(f"You have {training_points_str} strength points")
                                print("how many would you like to use: ")
                                use_str_point = int(input())
                                if use_str_point >= training_points_str:
                                    use_str_point = training_points_str
                                    current_point = pos4.get_strength()
                                    new_str = current_point + use_str_point
                                    pos4.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                elif use_str_point > 0 and use_str_point < training_points_str:
                                    current_point = pos4.get_strength()
                                    new_str = current_point + use_str_point
                                    pos4.set_strength(new_str)
                                    training_points_str -= use_str_point
                                    print(f"You increase your strength by {use_str_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 2:
                                print(f"You have {training_points_int} intellect points")
                                print("how many would you like to use: ")
                                use_int_point = int(input())
                                if use_int_point >= training_points_int:
                                    use_int_point = training_points_int
                                    current_point = pos4.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos4.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                elif use_int_point > 0 and use_int_point < training_points_int:
                                    current_point = pos4.get_intellect()
                                    new_int = current_point + use_int_point
                                    pos4.set_intellect(new_int)
                                    training_points_int -= use_int_point
                                    print(f"You increase your intellect by {use_int_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 3:
                                print(f"You have {training_points_speed} speed points")
                                print("how many would you like to use: ")
                                use_speed_point = int(input())
                                if use_speed_point >= training_points_speed:
                                    use_speed_point = training_points_speed
                                    current_point = pos4.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos4.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                elif use_speed_point > 0 and use_speed_point < training_points_speed:
                                    current_point = pos4.get_speed()
                                    new_speed = current_point + use_speed_point
                                    pos4.set_speed(new_speed)
                                    training_points_speed -= use_speed_point
                                    print(f"You increase your speed by {use_speed_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 4:
                                print(f"You have {candy_hp} HP Candy")
                                print("how many would you like to use: ")
                                use_hp_point = int(input())
                                if use_hp_point >= candy_hp:
                                    use_hp_point = candy_hp
                                    current_point = pos4.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos4.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                elif use_hp_point > 0 and use_hp_point < candy_hp:
                                    current_point = pos4.get_health()
                                    new_hp = current_point + use_hp_point
                                    pos4.set_health(new_hp)
                                    candy_hp -= use_hp_point
                                    print(f"You increase your HP by {use_hp_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 5:
                                print(f"You have {candy_def} Defense Candy")
                                print("how many would you like to use: ")
                                use_def_point = int(input())
                                if use_def_point >= candy_def:
                                    use_def_point = candy_def
                                    current_point = pos4.get_defense()
                                    new_def = current_point + use_def_point
                                    pos4.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                elif use_def_point > 0 and use_def_point < candy_def:
                                    current_point = pos4.get_defense()
                                    new_def = current_point + use_def_point
                                    pos4.set_defense(new_def)
                                    candy_def -= use_def_point
                                    print(f"You increase your defense by {use_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 6:
                                print(f"You have {candy_m_def} M Defense Candy")
                                print("how many would you like to use: ")
                                use_m_def_point = int(input())
                                if use_m_def_point >= candy_m_def:
                                    use_m_def_point = candy_m_def
                                    current_point = pos4.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos4.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                elif use_m_def_point > 0 and use_m_def_point < candy_m_def:
                                    current_point = pos4.get_m_defense()
                                    new_m_def = current_point + use_m_def_point
                                    pos4.set_m_defense(new_m_def)
                                    candy_m_def -= use_m_def_point
                                    print(f"You increase your m defense by {use_m_def_point}")
                                else:
                                    print("Please enter a positive number")
                            elif opt_menu_spend_P4 == 7:
                                hero.position_data(pos4)
                            else:
                                print("Invalid option")
                            team.spend_P4()
                            opt_menu_spend_P4 = int(input(" Enter your option >"))
                    elif opt_menu_spend_training == 5:
                        print(f"You have {training_points_str} strength training points")
                        print(f"You have {training_points_int} intellect training points")
                        print(f"You have {training_points_speed} speed training points")
                        print(f"You have {candy_hp} HP Candy")
                        print(f"You have {candy_def} Defense Candy")
                        print(f"You have {candy_m_def} M Defense Candy\n")
                        time.sleep(2)

                    else:
                        print("Invalid option")
                    team.spend_TP_menu()
                    opt_menu_spend_training = int(input(" Enter your option >"))

            else:
                print("Invalid option")
            team.training_menu()
            opt_menu_training = int(input(" Enter your option >"))

    elif option_menu == 2:
        team.shop_menu()
        opt_menu_shop = int(input(" Enter your option >"))
        while opt_menu_shop != 0:
            if opt_menu_shop == 1:
                if player_gold >= 100:
                    candy_def += 1
                    print(f"You bough 1 Defense Candy and now have {candy_def} Defense Candy")

                else:
                    print("You don't have enough gold")
            elif opt_menu_shop == 2:
                if player_gold >= 100:
                    candy_m_def += 1
                    print(f"You bough 1 Defense Candy and now have {candy_m_def} Defense Candy")

                else:
                    print("You don't have enough gold")

            elif opt_menu_shop == 3:
                if player_gold >= 100:
                    candy_hp += 1
                    print(f"You bough 1 Defense Candy and now have {candy_hp} Defense Candy")

                else:
                    print("You don't have enough gold")
            elif opt_menu_shop == 4:
                print("Coming soon")
            elif opt_menu_shop == 5:
                if player_artifacts >= 1:
                    player_artifacts -= 1
                    player_gold += 5000
                    print(f"You sold 1 Artifact Candy and now have {player_gold} Gold")

                else:
                    print("You don't have artifacts")

            else:
                print("Invalid option")
            team.shop_menu()
            opt_menu_shop = int(input(" Enter your option >"))
    elif option_menu == 3:

        print("Option 3 was selected")
        if team1_name == "":
            team1_name = input("Please enter your team's name\n")
        else:
            print(f" Welcome back {team1_name}")


        team1_hero_list = [t1hero1, t1hero2, t1hero3, t1hero4]
        team1_speed = t1hero1.get_speed() + t1hero2.get_speed() + t1hero3.get_speed() + t1hero4.get_speed()

        print(f"team 1 speed is {team1_speed}")
        team1 = {"heroP1": team1_hero_list[0].name, "heroP2": team1_hero_list[1].name, "heroP3": team1_hero_list[2].name,
                 "heroP4": team1_hero_list[3].name}
        team.team_display_menu(team1_name,team1)

    elif option_menu == 4:
        team.team_build_menu()
        opt_tb_menu = int(input(" Enter your option >"))
        while opt_tb_menu != 0:

            if opt_tb_menu == 1:
                print("Please enter your hero name for position 1")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero1 = team.get_hero(hero_id)
                t1hero1.set_bf_position("P1")
                print(t1hero1.get_bf_position())
                print(f"You assigned {t1hero1.get_name()} to position 1")

            elif opt_tb_menu == 2:
                print("Please enter your hero name for position 2")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero2 = team.get_hero(hero_id)
                t1hero2.set_bf_position("P2")
                print(t1hero2.get_bf_position())
                print(f"You assigned {t1hero2.get_name()} to position 2")

            elif opt_tb_menu == 3:
                print("Please enter your hero name for position 3")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero3 = team.get_hero(hero_id)
                t1hero3.set_bf_position("P3")
                print(t1hero3.get_bf_position())
                print(f"You assigned {t1hero3.get_name()} to position 3")

            elif opt_tb_menu == 4:
                print("Please enter your hero name for position 4")
                hero_name = input().strip().lower()
                hero_id = team.heroes_id_converter(hero_name)
                t1hero4 = team.get_hero(hero_id)
                t1hero4.set_bf_position("P4")
                print(t1hero4.get_bf_position())
                print(f"You assigned {t1hero4.get_name()} to position 4")

            elif opt_tb_menu == 5:
                team.hero_information_menu()
                opt_menu_h_inf = int(input(" Enter your option >"))
                while opt_menu_h_inf != 0:
                    if opt_menu_h_inf == 1:
                        #os.system('clear')
                        print("\nThese are the current heroes available")
                        info_hero_dict = {"adan": hero.Adan(), "alma": hero.Alma(), "franky": hero.Franky(), "luis": hero.Luis(), "kakashi": hero.Chino(), "lee": hero.Gil(), "itachi": hero.Lalo(), "ino": hero.Sherman()}
                        hero_list_info = ["Adan", "Alma", "Franky", "Luis", "Kakashi", "Lee", "Itachi", "Ino"]
                        print(hero_list_info)

                        print("\nPlease enter your hero name to show information\n")
                        hero_name = input().strip().lower()
                        test_hero = info_hero_dict[hero_name]
                        hero.hero_data(test_hero)
                    else:
                        print("Invalid option")
                    print()
                    team.hero_information_menu()
                    opt_menu_h_inf = int(input(" Enter your option >"))
                time.sleep(2)
            else:
                print("Invalid option")
            print()
            team.team_build_menu()
            opt_tb_menu = int(input(" Enter your option"))

    elif option_menu == 5:
        temp_t1hero1_HP = t1hero1.get_health()
        temp_t1hero2_HP = t1hero2.get_health()
        temp_t1hero3_HP = t1hero3.get_health()
        temp_t1hero4_HP = t1hero4.get_health()

        team1_hero_list = [t1hero1, t1hero2, t1hero3, t1hero4]
        team1_speed = t1hero1.get_speed() + t1hero2.get_speed() + t1hero3.get_speed() + t1hero4.get_speed()


        # defining Enemy Team
        level_e_list = level_1_fire()
        t2hero1 = level_e_list[0]
        t2hero2 = level_e_list[1]
        t2hero3 = level_e_list[2]
        t2hero4 = level_e_list[3]

        team2_name = "Fire Team 1"
        # team2_hero_list = [t2hero1, t2hero2, t2hero3, t2hero4]
        team2_speed = t2hero1.get_speed() + t2hero2.get_speed() + t2hero3.get_speed() + t2hero4.get_speed()
        print(f"team 2 speed is {team2_speed}")

        team2 = {"heroM": t2hero1.get_name(), "heroS1": t2hero3.get_name(), "heroS2": t2hero4.get_name(),
                 "heroS3": t2hero2.get_name()}
        round = 1
        print(f"Round {round}")
        combat.battle_menu()
        opt_menu_combat = int(input(" Enter your option >"))
        while opt_menu_combat != 0:
            if opt_menu_combat == 1:
                print("Coming soon")
            elif opt_menu_combat == 2:
                team.team_display(team1_name, team1, team2_name, team2)
            elif opt_menu_combat == 3:

                print(f"{t1hero1.get_name()} and {t2hero1.get_name()} step in for battle")
                time.sleep(2)
                combat_stats(t1hero1, t2hero1)
                # a_move = "kinto_attack"

            elif opt_menu_combat == 4:

                print(f"{t1hero1.get_name()} and {t2hero1.get_name()} step in for battle")
                time.sleep(2)
                combat_stats(t1hero1, t2hero1)

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

            elif opt_menu_combat == 5:
                round +=1
                print(f"Round {round}")
                combat.reset_round_var(t1hero1, t1hero2, t1hero3, t1hero4)
                combat.reset_round_var(t2hero1, t2hero2, t2hero3, t2hero4)
            else:
                print("Invalid option")
            print()
            combat.battle_menu()
            opt_menu_combat = int(input(" Enter your option >"))

        t1hero1.set_health(temp_t1hero1_HP)
        t1hero2.set_health(temp_t1hero2_HP)
        t1hero3.set_health(temp_t1hero3_HP)
        t1hero4.set_health(temp_t1hero4_HP)


    else:
        print("Invalid option")
    print()
    team.Game_Menu()
    option_menu = int(input(" Enter your option"))

exit()
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

team2_name = "Fire Team 1"
#team2_hero_list = [t2hero1, t2hero2, t2hero3, t2hero4]
team2_speed = t2hero1.get_speed() + t2hero2.get_speed() + t2hero3.get_speed() + t2hero4.get_speed()
print(f"team 2 speed is {team2_speed}")

team2 = {"heroM": t2hero1.get_name(), "heroS1": t2hero3.get_name(), "heroS2": t2hero4.get_name(),
         "heroS3": t2hero2.get_name()}



#function to display team information, hero position, and battling hero

def main():
    battle()

main()










# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
