# This page will have all the heroes dictionaries

# Hero class with all standard attributes

class Hero():
  def __init__(self):
    self.stats = {"health points": 1200.0,
                  "defense": 20,
                  "m_defense": 20,
                  "strength": 25,
                  "intellect": 10,
                  "speed": 5}
      
    self.battle_field = {"position": {"main": False, "support1": False, "support2": False, "support3": False}}
    self.element = ""
    self.state = {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
    self.level = 1
    self.xp = 0
    self.held_items = {}
    self.name = ""
    self.move = {}
    self.attacked = False
    self.alive = True


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
    self.move = {
          "kinto_attack": {
                          "name": "Mega Punch",
                          "damage": 24,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "knockdown",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Slash",
                          "damage": 5,
                          "chase": "knockdown",
                          "cause": "repulsed",
                          "type": "str",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Heal",
                    "power": 14,
                    "cause": "normal",
                    "type": "int"
                    },
        "passive": {
                    "name": "40/40",
                    "action": 35,
                    "type": "boost"
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
                          "damage": 24,
                          "cost": 2,
                          "cool-down": 1,
                          "cause": "PA",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Scream",
                          "damage": 5,
                          "chase": "confused",
                          "cause": "knockdown",
                          "type": "int",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Chaos",
                    "power": 14,
                    "cause": "stunt",
                    "type": "int"
                    },
        "passive": {
                    "name": "sprinting",
                    "action": 35,
                    "type": "boost"
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
                          "type": "int"
                          },
        "standard_attack": {
                    "name": "Mist",
                    "power": 14,
                    "cause": "normal",
                    "type": "int"
                    },
        "passive": {
                    "name": "Medical knowledge",
                    "action": 1.2,
                    "type": "boost"
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
                          "damage": 30,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Hyper punch",
                          "damage": 8,
                          "chase": "knockdown",
                          "cause": "knockdown",
                          "type": "str",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Mud armor",
                    "power": 10,
                    "cause": "Immunity",
                    "type": "int"
                    },
        "passive": {
                    "name": "Earth master",
                    "action": 1.35,
                    "type": "boost"
                    }
        }
class Chino(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Jaime Leyva"
    self.element = "Lighting"
    self.move = {
          "kinto_attack": {
                          "name": "Kamui",
                          "damage": 30,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "type": "int"
                          },
        "chase_attack": {
                          "name": "One Thousand Years of Death",
                          "damage": 8,
                          "chase": "Repulsed",
                          "cause": "high float",
                          "type": "str",
                          "used": False
                          },
        "standard_attack": {
                            "name": "Lighting Blade",
                            "power": 5,
                            "cause": "low float",
                            "type": "str/int"
                    },
        "passive": {
                    "name": "Ambition",
                    "action": 1.05,
                    "type": "boost"
                    }
        }

class Gil(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.name = "Gil Osuna"
    self.element = "Earth"
    self.move = {
          "kinto_attack": {
                          "name": "Konoha Hurricane",
                          "damage": 44,
                          "cost": 3,
                          "cool-down": 2,
                          "cause": "repulsed",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Primary Lotus",
                          "damage": 9,
                          "chase": "high float",
                          "cause": "knockdown",
                          "used": False
                          },
        "standard_attack": {
                            "name": "Taijutsu Attack",
                            "power": 5,
                            "cause": "high float",
                            "type": "str"
                    },
        "passive": {
                    "name": "Gate of Joy",
                    "action": 0.25,
                    "type": "boost"
                    }
        }

class Lalo(Hero):
  def __init__(self):
    Hero.__init__(self)
    self.stats["speed"] = 10
    self.name = "Eduardo Castro"
    self.element = "Fire"
    self.move = {
        "kinto_attack": {
                          "name": "Moonlight Slash",
                          "damage": 36,
                          "cost": 2,
                          "cool-down": 2,
                          "cause": "knockdown",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Amaterasu",
                          "damage": 6,
                          "chase": "high float",
                          "cause": "burning",
                          "type": "int",
                          "used": False
                          },
        "standard_attack": {
                           "name": "Crow dance",
                           "power": 5,
                           "cause": "high float",
                           "type": "str/int"
                            },
        "passive": {
                    "name": "Coordinated combat",
                    "action": 1.30,
                    "type": "boost"
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
                          "damage": 26,
                          "cost": 1,
                          "cool-down": 1,
                          "cause": "burning",
                          "type": "str"
                          },
        "chase_attack": {
                          "name": "Look-down",
                          "damage": 4,
                          "chase": "burning",
                          "cause": "knockdown",
                          "type": "int",
                          "used": False
                          },
        "standard_attack": {
                    "name": "Mom's Food",
                    "power": 13,
                    "type": "int",
                    "cause": "normal"
                    },
        "passive": {
                    "name": "Physics PhD",
                    "action": 1.05 ,
                    "type": "boost"
                    }
        }

