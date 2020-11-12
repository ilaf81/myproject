import os
# This page will have all the heroes dictionaries

# Hero class with all standard attributes

def position_data(position):
    pos = position
    print("---------- Position Information ---------- ")
    print(f"""
   ---------Base stats----------
   {pos.get_name().ljust(15)}                                                 
   HP: {str(pos.get_health()).ljust(15)}                                                 
   DEF: {str(pos.get_defense()).ljust(15)}
   MDF: {str(pos.get_m_defense()).ljust(15)}
   STR: {str(pos.get_strength()).ljust(15)}
   INT: {pos.get_intellect()} 
   SPD: {pos.get_speed()} 
    """)

def hero_data( hero):

    adan = hero

    print("---------- Hero Information ---------- ")
    print(f"""
    ---------Base stats----------
    {adan.get_name().ljust(15)}                    INT: {adan.get_intellect()}                              
    HP: {str(adan.get_health()).ljust(15)}                SPD: {adan.get_speed()}                                  
    DEF: {str(adan.get_defense()).ljust(15)}               ELM: {adan.get_element().ljust(15)}                          
    STR: {str(adan.get_strength()).ljust(15)}               HID: {adan.get_id()}                           
    ----------Moves----------
    KTN: {adan.move["kinto_attack"]["name"].ljust(15)}          CHA: {adan.move["chase_attack"]["name"].ljust(15)}      
         DMG: {str(adan.move["kinto_attack"]["damage"]).ljust(15)}          DMG: {adan.move["chase_attack"]["damage"]}                         
         CST: {str(adan.move["kinto_attack"]["cost"]).ljust(15)}          CHA: {adan.move["chase_attack"]["chase"]}                        
         DTP: {str(adan.move["kinto_attack"]["type"]).ljust(15)}          CAU: {adan.move["chase_attack"]["cause"]} 
                                            DTP: {adan.move["chase_attack"]["type"]}
   
    STD: {adan.move["standard_attack"]["name"].ljust(15)}           PAS: {adan.move["passive"]["name"].ljust(15)} 
         DMG: {str(adan.move["standard_attack"]["power"]).ljust(15)}           DES: {adan.move["passive"]["desc"]}                                           
         CAU: {adan.move["standard_attack"]["cause"]}
         DTP: {adan.move["standard_attack"]["type"]}
                                        
         
            """)

#creating a class for the position on battle field

class Position():
    def __init__(self):
        self.name = "P"
        self.health = 0
        self.intellect = 0
        self.strength = 0
        self.defense = 0
        self.m_defense = 0
        self.speed = 0
    # function to get name
    def get_name(self):
        return self.name

    # function to get speed
    def get_speed(self):
        return self.speed

    # function to get speed
    def set_speed(self, spd_var):
        self.speed = spd_var

    # function to get health
    def get_health(self):
        return self.health

    # function to set health
    def set_health(self, new_hp):
        self.health = new_hp

    # function to get defense

    def get_defense(self):
        return self.defense
    # function to update defense
    def set_defense(self, new_def):
        self.defense = new_def

    # function to get magic defense

    def get_m_defense(self):
        return self.m_defense

    # function to update magic defense

    def set_m_defense(self, new_m_def):
        self.m_defense = new_m_def

    # function to get intellect

    def get_intellect(self):
        return self.intellect

    # function to update intellect

    def set_intellect(self, new_int):
        self.intellect = new_int

    # function to get strength

    def get_strength(self):
        return self.strength

    # function to update strength

    def set_strength(self, new_str):
        self.strength = new_str

class P1(Position):
    def __init__(self):
        Position.__init__(self)
        self.name = "Position 1"
        self.health = 200
        self.defense = 100
        self.m_defense = 100
class P2(Position):
    def __init__(self):
        Position.__init__(self)
        self.strength = 150
        self.name = "Position 2"

class P3(Position):
    def __init__(self):
        Position.__init__(self)
        self.speed = 100
        self.strength = 50
        self.intellect = 50
        self.name = "Position 3"

class P4(Position):
    def __init__(self):
        Position.__init__(self)
        self.intellect = 150
        self.name = "Position 4"

class Hero():
  def __init__(self):
    self.stats = {"health points": 1200.0,
                  "defense": 20,
                  "m_defense": 20,
                  "strength": 25,
                  "intellect": 10,
                  "speed": 5}
      
    self.battle_field = ""
    self.element = ""
    self.state = {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
    self.level = 1
    self.xp = 0
    self.held_items = {}
    self.name = ""
    self.move = {}
    self.attacked = False
    self.alive = True
    self.id = 0

  #function to get position
  def get_bf_position(self):
      return self.battle_field

  #function to get position
  def set_bf_position(self, position):
      self.battle_field = position
  #function to get hero unique id
  def get_id(self):
      return self.id

  #function to get hero name
  def get_name(self):
    return self.name

  #function to get hero speed
  def get_speed(self):
    return self.stats["speed"]

  #function to get hero health
  def get_health(self):
    return self.stats["health points"]

  #function to set health
  def set_health(self, new_hp):
    self.stats["health points"] = new_hp

  #function to get defense
  def get_defense(self):
    return self.stats["defense"]

  #function to update defense
  def set_defense(self, new_def):
    self.stats["defense"] = new_def

  #function to get magic defense
  def get_m_defense(self):
    return self.stats["m_defense"]

  #function to update magic defense
  def set_m_defense(self, new_m_def):
    self.stats["m_defense"] = new_m_def

  #function to get intellect
  def get_intellect(self):
    return self.stats["intellect"]

  #function to update intellect
  def set_intellect(self, new_int):
    self.stats["intellect"] = new_int

  # function to get strength
  def get_strength(self):
    return self.stats["strength"]

  # function to update strength
  def set_strength(self, new_str):
    self.stats["strength"] = new_str
  # function to check if plater already attacked
  def get_attacked(self):
      return self.attacked

  def set_attacked(self, is_attacked):
      self.attacked = is_attacked

  def get_element(self):
    return self.element


class Adan(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Adan Cruz"
    self.element = "Fire"
    self.id = 1
    self.move = {
          "kinto_attack": {
                          "name": "Mega Punch",
                          "damage": 24,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "knockdown",
                          "type": "str",
                          "heals": False
                          },
        "chase_attack": {
                          "name": "Slash",
                          "damage": 5,
                          "chase": "knockdown",
                          "cause": "repulsed",
                          "type": "str",
                          "used": False,
                          "heals": False
                          },
        "standard_attack": {
                    "name": "Heal",
                    "power": 14,
                    "cause": "cured",
                    "heals": True,
                    "type": "int"
                    },
        "passive": {
                    "name": "40/40",
                    "action": 1.35,
                    "type": "strength",
                    "desc": "Increase strength 35%"
                    }
        }

class Franky(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Franky Cruz"
    self.element = "Wind"
    self.id = 2
    self.move = {
          "kinto_attack": {
                          "name": "Mega Kick",
                          "damage": 24,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "PA",
                          "heals": False,
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Scream",
                          "damage": 5,
                          "chase": "confused",
                          "cause": "knockdown",
                          "heals": False,
                          "type": "int",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Chaos",
                    "power": 14,
                    "cause": "stunt",
                    "heals": False,
                    "type": "int"
                    },
        "passive": {
                    "name": "Sprinting",
                    "action": 1.35,
                    "type": "speed",
                    "desc": "Increase speed 35%"
                    }
        }

class Alma(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Alma Cruz"
    self.element = "Water"
    self.id = 3
    self.move = {
          "kinto_attack": {
                          "name": "Water Fall",
                          "damage": 24,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "poisoning",
                          "type": "int"
                          },
        "chase_attack": {
                          "name": "Kick",
                          "damage": 5,
                          "chase": "repulsed",
                          "cause": "confused",
                          "used": False,
                          "heals": False,
                          "type": "int"
                          },
        "standard_attack": {
                    "name": "Mist",
                    "power": 14,
                    "cause": "normal",
                    "heals": True,
                    "type": "int"
                    },
        "passive": {
                    "name": "Medical knowledge",
                    "action": 1.35,
                    "type": "intellect",
                    "desc": "Increase intellect 35%"
                    }
        }

class Luis(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Luis Cruz"
    self.element = "Earth"
    self.id = 4
    self.move = {
          "kinto_attack": {
                          "name": "Earthquake",
                          "damage": 30,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "heals": False,
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Hyper punch",
                          "damage": 8,
                          "chase": "knockdown",
                          "cause": "knockdown",
                          "type": "str",
                          "heals": False,
                          "used": False
                          },
        "standard_attack": {
                    "name": "Mud armor",
                    "power": 10,
                    "cause": "Immunity",
                    "heals": True,
                    "type": "int"
                    },
        "passive": {
                    "name": "Earth master",
                    "action": 1.35,
                    "type": "strength",
                    "desc": "Increase strength 35%"
                    }
        }
class Chino(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Kakashi" # Jaime Leyva
    self.element = "Lighting"
    self.id = 5
    self.move = {
          "kinto_attack": {
                          "name": "Kamui",
                          "damage": 30,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "heals": False,
                          "type": "int"
                          },
        "chase_attack": {
                          "name": "One Thousand Years of Death",
                          "damage": 8,
                          "chase": "Repulsed",
                          "cause": "high float",
                          "type": "str",
                          "used": False,
                          "heals": False
                          },
        "standard_attack": {
                            "name": "Lighting Blade",
                            "power": 5,
                            "cause": "low float",
                            "heals": False,
                            "type": "str/int"
                    },
        "passive": {
                    "name": "Ambition",
                    "action": 1.25,
                    "type": "m_defense",
                    "desc": "Increase magic defense 25%"
                    }
        }

class Gil(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Lee" # Gil Osuna
    self.element = "Earth"
    self.id = 6
    self.move = {
          "kinto_attack": {
                          "name": "Konoha Hurricane",
                          "damage": 44,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "repulsed",
                          "heals": False,
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Primary Lotus",
                          "damage": 9,
                          "chase": "high float",
                          "cause": "knockdown",
                          "heals": False,
                          "type": "str",
                          "used": False
                          },
        "standard_attack": {
                            "name": "Taijutsu Attack",
                            "power": 5,
                            "cause": "high float",
                            "heals": False,
                            "type": "str"
                    },
        "passive": {
                    "name": "Gate of Joy",
                    "action": 1.25,
                    "type": "defense",
                    "desc": "Increase defense 25%"
                    }
        }

class Lalo(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.stats["speed"] = 10
    self.name = "Itachi" # Eduardo Castro
    self.element = "Fire"
    self.id = 7
    self.move = {
        "kinto_attack": {
                          "name": "Moonlight Slash",
                          "damage": 36,
                          "cost": 2,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "heals": False,
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Amaterasu",
                          "damage": 6,
                          "chase": "high float",
                          "cause": "burning",
                          "type": "int",
                          "heals": False,
                          "used": False
                          },
        "standard_attack": {
                           "name": "Crow dance",
                           "power": 5,
                           "cause": "high float",
                           "heals": False,
                           "type": "str/int"
                            },
        "passive": {
                    "name": "Coordinated combat",
                    "action": 1.35,
                    "type": "strength",
                    "desc": "Increase strength 35%"
                    }
        }


class Sherman(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Ino" # Carlos Duarte
    self.element = "Earth"
    self.id = 8
    self.move = {
          "kinto_attack": {
                          "name": "Hand Shake",
                          "damage": 26,
                          "cost": 1,
                          "cool-down": 1,
                          "cause": "burning",
                          "heals": False,
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Look-down",
                          "damage": 4,
                          "chase": "burning",
                          "cause": "knockdown",
                          "heals": False,
                          "type": "int",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Mom's Food",
                    "power": 13,
                    "type": "int",
                    "heals": True,
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Physics PhD",
                    "action": 1.35,
                    "type": "boost",
                    "desc": "Increase intellect 35%"
                    }
        }

