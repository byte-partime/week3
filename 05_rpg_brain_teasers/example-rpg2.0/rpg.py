import random
from view import View
from model import *


class GameController:
    def __init__(self):
        self.missions = []
        self.player = None
        self.dungeon = []
        self.view = View()

    def start(self):
        self.view.welcome_message()
        self.load_map()
        choice = self.view.login_or_register()
        if choice == 0:
            self.login()
        elif choice == 1:
            self.register()

    def create_player(self):
        username = self.view.input_username()
        password = self.view.input_password()
        name = self.view.input_player_name()
        race = "robot"
        return Player(username, password, name, race)

    def load_map(self):
        self.dungeon.append(Room(0,"You open you eyes. You find yourself in an empty laboratory. Oh snap! While looking down at your arms and legs, you realize that you are a robot! There are wires and circuit components and whatnot. Oh dear....  After stuggling with existential thoughts for a minute, you get a hold of yourself. There is an exit to the north.", 1, None, None, None, None))

        self.dungeon.append(Room(1, "You enter a dark hallway. There is a portrait of a scientist hanging on the wall. There is one door to the west, and another to the east.", None, 3, None, 2, None))

        newmission = Mission("You hear a rustling noise behind the desk. Do you want to investigate it?", ["yes", "no"], 1)
        self.dungeon.append(Room(2, "You enter a nice looking office. There is a desk with a computer on it.", None, 1, None, None, newmission))

        newmission = Mission("You hear a buzzing sound coming from the closet. Check it out?", ["yes", "no"], 2)
        self.dungeon.append(Room(3, "You enter another laboratory room. There are robot parts scattered around, and there is blood all over the place. There is a closet in the corner of the room.", None, None, None, 1, newmission))

    
    def play(self):
        while self.player.map_index != None:
            self.enter_room(self.dungeon[self.player.map_index])
    
    def enter_room(self, room):
        self.view.room_description(room)
        if room.mission != None and not room.mission_passed:
            mission_result = room.mission.start(self.player)
            if mission_result == True:
                room.mission_passed = True
            elif mission_result == False:
                self.view.player_died_message()
                #reset game state when player dies
                self.player.map_index = 0
        actions = ["north", "east", "south", "west", "quit"]
        decision = self.view.input_room_decision(actions)
        
        if decision == "north" and room.north != None:
            self.player.map_index = room.north
        elif decision == "east" and room.east != None:
            self.player.map_index = room.east
        elif decision == "south" and room.south != None:
            self.player.map_index = room.south
        elif decision == "west" and room.west != None:
            self.player.map_index = room.west
        elif decision == "quit":
            self.player.map_index = None
            self.view.quit_game(self.player)
            return
        else:
            self.view.wrong_way_message(decision)
        self.player.update()
        


    def register(self):   
        while True:
            self.player = self.create_player()
            if Player.username_available(self.player.username):
                break
        self.player.insert()

    def login(self):
        while True:
            username = self.view.input_username()
            password = self.view.input_password()

            self.player = Player()
            if self.player.load(username, password):
                break
            else:
                self.view.login_incorrect_message()


class Mission:
    def __init__(self, description, actions, level):
        self.description = description
        self.actions = actions
        self.level = level
        self.view = View()

    def start(self, player):
        self.player = player
        self.view.mission_description(self.description)
       
        decision = self.view.input_mission_decision(self.actions)
        
        passed_mission = self.determine_outcome(decision)
        if passed_mission:
            battle = Battle(self.player, self.level)
            self.view.battle_started_message(battle.monster.race)
            while battle.take_turn():
                pass
            if battle.lost == False:
                return True
        elif passed_mission == False:
            return None
        return False

    #TODO make random decision
    def determine_outcome(self, action):
        if action not in self.actions:
            return None
        elif action == self.actions[0]:
            return True
        else:
            return False


class Battle:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.monster = MonsterFactory.create(level)
        self.is_players_turn = bool(random.getrandbits(1))
        self.lost = False
        self.view = View()

    def take_turn(self):
        if self.is_players_turn:
            choice = self.view.battle_decision()
            if choice == 0:
                return self.player_attack()
            elif choice == 1:
                return self.block_attack()
            elif choice == 2:
                return self.flee()
        elif not self.is_players_turn:
            return self.monster_attack()

    def monster_attack(self):
        self.view.got_attacked_message(self.monster.race, self.monster.attack)
        self.player.take_damage(self.monster.attack)
        self.is_players_turn = True
        if self.player.is_dead():
            self.view.player_died_message()
            self.lost = True
            return False
        self.view.player_health_message(self.player.hp)
        return True


    def player_attack(self):
        self.monster.take_damage(self.player.attack)
        if self.monster.is_dead():
            self.player.exp += self.monster.exp
            self.view.killed_monster_message(self.monster, self.player)
            return False
        else:
            self.view.attacked_monster_message(self.monster.race, self.player.attack)
            self.is_players_turn = False
            return True

    def block_attack(self):
        self.view.blocked_attack_message()
        self.is_players_turn = True
        return True

    def flee(self):
        able_to_flee = bool(random.getrandbits(1))
        if able_to_flee:
            self.view.ran_away_message()
            return False
        else:
            self.view.couldnt_run_away_message()
            self.is_players_turn = False
            return True


game = GameController()
game.start()
game.play()

