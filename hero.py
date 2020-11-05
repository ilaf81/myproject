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

  def get_name(self):
    return self.name

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
                          "name": "Kick 1",
                          "damage": 5,
                          "chase": "poisoning",
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


gil_hero = {
  "health points": 120,
  "defense": 20,
  "m_defense": 20,
  "strength": 25,
  "intellect": 10,
  "speed": 5,
  "position": {"main": "front", "support": "rear"},
  "element": "lighting",
  "state": {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
  "base_experience": 100,
  "height": 3,
  "held_items": {},
  "id": 5,
  "moves": [
    {
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
        "power": 35
      }
    }],
  "name": "Gil Osuna",
  "weight": 90
  }
lalo_hero = {
  "health points": 120,
  "defense": 20,
  "m_defense": 20,
  "strength": 25,
  "intellect": 10,
  "speed": 5,
  "position": {"main": "front", "support": "rear"},
  "element": "fire",
  "state": {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
  "base_experience": 100,
  "height": 3,
  "held_items": {},
  "id": 6,
  "moves": [
    {
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
        "power": 35
      }
    }],
  "name": "Eduardo Castro",
  "weight": 90
  }
sherman_hero = {
  "health points": 120,
  "defense": 20,
  "m_defense": 20,
  "strength": 25,
  "intellect": 10,
  "speed": 5,
  "position": {"main": "front", "support": "rear"},
  "element": "earth",
  "state": {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
  "base_experience": 100,
  "height": 3,
  "held_items": {},
  "id": 7,
  "moves": [
    {
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
        "power": 35
      }
    }],
  "name": "Carlos Duarte",
  "weight": 90
  }
chino_hero = {
  "health points": 120,
  "defense": 30,
  "m_defense": 20,
  "strength": 25,
  "intellect": 10,
  "speed": 5,
  "position": {"main": "front", "support": "rear"},
  "element": "wind",
  "state": {"normal": True, "poisoning": False, "stunt": False, "burning": False, "confused": False},
  "base_experience": 100,
  "height": 3,
  "held_items": {},
  "id": 8,
  "moves": [
    {
      "kinto_attack": {
        "name": "Mega Kick",
        "damage": 12,
        "cost": 2,
        "cool-down": 1,
        "cause": "PA",
        "type": "atk"
      },
      "chase_attack": {
        "name": "Dash 1",
        "damage": 5,
        "chase": "PA",
        "cause": "KD",
        "type": "atk/matk"
      },
      "support": {
        "name": "shield 1",
        "power": 24,
      },
      "passive": {
        "name": "cheetah",
        "power": 35
      }
    }],
  "name": "Jaime Leyva",
  "weight": 90
  }
