# This page will have all the heroes dictionaries

# Hero class with all standard attributes

class Hero():
  def __init__(self):
    self.stats = {"health points": 120,
                  "defense": 20,
                  "m_defense": 20,
                  "strength": 25,
                  "intellect": 10,
                  "speed": 5}
      
    self.battle_field = {"position": {"main": False, "support1": False, "support2": True, "support3": True}}
    self.element = ""
    self.state = {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
    self.level = 1
    self.xp = 0
    self.held_items = {}
    self.name = ""
    self.move = {}

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



class Adan(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Adan Cruz"
    self.element = "Fire"
    self.move = {
          "kinto_attack": {
                          "name": "Mega Punch",
                          "damage": 12,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "PA"
                          },
        "chase_attack": {
                          "name": "Slash 1",
                          "damage": 5,
                          "chase": "PA",
                          "cause": "KD"
                          },
        "support": {
                    "name": "heal 1",
                    "power": 14,
                    },
        "passive": {
                    "name": "40/40",
                    "critical hit": 35
                    }
        }

class Franky(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Franky Cruz"
    self.element = "Wind"
    self.move = {
          "kinto_attack": {
                          "name": "Mega Kick",
                          "damage": 12,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "PA"
                          },
        "chase_attack": {
                          "name": "Scream 1",
                          "damage": 5,
                          "chase": "PA",
                          "cause": "KD"
                          },
        "support": {
                    "name": "chaos 1",
                    "power": 14,
                    "cause": "stunt"
                    },
        "passive": {
                    "name": "sprinting",
                    "speed": 35
                    }
        }

class Alma(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Alma Cruz"
    self.element = "Water"
    self.move = {
          "kinto_attack": {
                          "name": "Water Fall",
                          "damage": 12,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "poisoning"
                          },
        "chase_attack": {
                          "name": "Kick",
                          "damage": 5,
                          "chase": "PA",
                          "cause": "KD"
                          },
        "support": {
                    "name": "Mist 1",
                    "power": 14,
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Medical knowledge",
                    "heals %": 1.2
                    }
        }

class Luis(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Luis Cruz"
    self.element = "Earth"
    self.move = {
          "kinto_attack": {
                          "name": "Earthquake",
                          "damage": 15,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "KD"
                          },
        "chase_attack": {
                          "name": "Hyper punch 1",
                          "damage": 8,
                          "chase": "KD",
                          "cause": "KD"
                          },
        "support": {
                    "name": "Mud armor",
                    "defense shield": 10,
                    "cause": "Immunity"
                    },
        "passive": {
                    "name": "Earth Master",
                    "str/int 35%": 1.35
                    }
        }
class Chino(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Jaime Leyva"
    self.element = "Wind"
    self.move = {
          "kinto_attack": {
                          "name": "Earthquake",
                          "damage": 15,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "KD"
                          },
        "chase_attack": {
                          "name": "Hyper punch 1",
                          "damage": 8,
                          "chase": "KD",
                          "cause": "KD"
                          },
        "support": {
                    "name": "Mud armor",
                    "defense shield": 10,
                    "cause": "Immunity"
                    },
        "passive": {
                    "name": "Earth Master",
                    "str/int 35%": 1.35
                    }
        }

class Gil(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Gil Osuna"
    self.element = "Water"
    self.move = {
          "kinto_attack": {
                          "name": "Triple kick",
                          "damage": 15,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "PA"
                          },
        "chase_attack": {
                          "name": "Upper Kick 1",
                          "damage": 8,
                          "chase": "PA",
                          "cause": "KD"
                          },
        "support": {
                    "name": "Ramen bowl",
                    "recover mana": 2,
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Earth Master",
                    "str/int 35%": 1.35
                    }
        }

class Lalo(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Eduardo Castro"
    self.element = "Fire"
    self.move = {
          "kinto_attack": {
                          "name": "Red Roses",
                          "damage": 18,
                          "cost": 2,
                          "cool-down": 2,
                          "cause": "PA"
                          },
        "chase_attack": {
                          "name": "Sweet Talk 1",
                          "damage": 5,
                          "chase": "PA",
                          "cause": "confused"
                          },
        "support": {
                    "name": "King Gambit",
                    "recover mana": 2,
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Chess Master",
                    "int 15%": 1.15
                    }
        }


class Sherman(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Carlos Duarte"
    self.element = "Earth"
    self.move = {
          "kinto_attack": {
                          "name": "Hand Shake",
                          "damage": 13,
                          "cost": 1,
                          "cool-down": 1,
                          "cause": "burning"
                          },
        "chase_attack": {
                          "name": "Look-down",
                          "damage": 4,
                          "chase": "burning",
                          "cause": "KD"
                          },
        "support": {
                    "name": "Mom's Food",
                    "heal": 13,
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Physics PhD",
                    "Team 5% speed": 1.05
                    }
        }

