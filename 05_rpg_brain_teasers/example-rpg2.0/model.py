import sqlite3

class Player:
    def __init__(self, username = "", password = "", name = "", race = ""):
        self.username = username
        self.password = password
        self.name = name
        self.race = race
        self.hp = 10
        self.exp = 0
        self.attack = 1 
        self.weapon = None 
        self.map_index = 0
        self.inventory = Inventory()

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

    def update(self):
        conn = sqlite3.connect("rpg.db")
        c = conn.cursor()
        c.execute(
            """
            UPDATE players SET 
                hp = ?,
                exp = ?,
                attack = ?,
                weapon = ?,
                map_index = ?
            WHERE username = ?
            """,(self.hp, self.exp, self.attack, self.weapon, self.map_index, self.username))
        conn.commit()
        c.close()

    def insert(self):
        conn = sqlite3.connect("rpg.db")
        c = conn.cursor()
        c.execute(
            """
            INSERT INTO players (username, password, name, race, hp, exp, attack, weapon, map_index) VALUES (?,?,?,?,?,?,?,?,?)
            """,(self.username, self.password, self.name, self.race, self.hp, self.exp, self.attack, self.weapon, self.map_index))
        conn.commit()
        c.close()

    def load(self, username, password):
        conn = sqlite3.connect("rpg.db")
        c = conn.cursor() 
        c.execute(
            """
            SELECT 
                username,
                password,
                name,
                race,
                hp,
                exp,
                attack,
                weapon,
                map_index            
            FROM players WHERE username=? AND password=?
            """,(username, password)       
        )
        row = c.fetchone()
        conn.commit()
        c.close()
        if row != None:
            self.username = row[0]
            self.password = row[1]
            self.name = row[2]
            self.race = row[3]
            self.hp = row[4]
            self.exp = row[5]
            self.attack = row[6]
            self.weapon = row[7]
            self.map_index = row[8]
            return True
        return False

    @classmethod
    def username_available(cls, username):
        conn = sqlite3.connect("rpg.db")
        c = conn.cursor() 
        c.execute(
            """
            SELECT 
                username
            FROM players WHERE username=?
            """,(username, )       
        )
        row = c.fetchone()
        conn.commit()
        c.close()
        if row == None:
            return True
        else:
            return False






class MonsterFactory:
    @classmethod
    def create(cls, level):
        if level == 1:
            return ZombieKitten()
        elif level == 2:
            return Drone()
        elif level == 5:
            return RoboCop()
        elif level == 10:
            return RoboNinja()

class Monster:
    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

class ZombieKitten(Monster):
    def __init__(self):
        self.hp = 1
        self.attack = 1
        self.race = "Zombie Kitten"
        self.attack_method = "Sharp Claws"
        self.exp = 1

class Drone(Monster):
    def __init__(self):
        self.hp = 2
        self.attack = 2
        self.race = "Drone"
        self.exp = 2

class RoboCop(Monster):
    def __init__(self):
        self.hp = 5
        self.attack = 5
        self.race = "RoboCop"
        self.exp = 5

class RoboNinja(Monster):
    def __init__(self):
        self.hp = 10
        self.attack = 10
        self.race = "Robo-Ninja"
        self.exp




class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item.name in items:
            items[item.name] += 1
        else:
            items[item.name] = 1
        
class InventoryItem:
    def __init__(self):
        pass

class Weapon(InventoryItem):
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

class Potion(InventoryItem):
    def __init__(self):
        pass

class HealingPotion(Potion):
    def __init__(self, name, hp):
        self.hp = hp
        self.name = name
  


class Room:
    def __init__(self, room_id, description, north, east, south, west, mission):
        self.room_id = room_id
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.mission = mission
        self.mission_passed = False

        


