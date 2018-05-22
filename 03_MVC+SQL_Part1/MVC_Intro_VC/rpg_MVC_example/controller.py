import random
from view import View


class Game:
    def __init__(self):
        self.mission_index = 0
        self.missions = []
        self.player = None
        self.view = View()

    def start(self):
        self.player = self.create_player()

    def create_player(self):
        name = self.view.input_player_name()
        race = self.view.input_player_race()
        return Player(name, race)

    def play(self):
        self.view.introduction_message()
        while self.mission_index < len(self.missions):
            if self.missions[self.mission_index].start(self.player):
                self.mission_index += 1
                self.view.passed_mission_message()
            else:
                self.view.failed_mission_message()
                break

    def load_missions(self, missions):
        self.missions = missions
        self.mission_index = 0



class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hp = 10
        self.attack = 1
    
    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0



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
            while battle.take_turn():
                pass
            if battle.lost == False:
                return True
        return False

    #TODO make random decision
    def determine_outcome(self, action):
        if action not in self.actions:
            return None
        elif action == self.actions[0]:
            return True
        else:
            return False



class MonsterFactory:
    @classmethod
    def create(cls, level):
        if level == 1:
            return Goblin()
        elif level == 2:
            return Orc()
        elif level == 5:
            return Troll()
        elif level == 10:
            return Balrog()



class Monster:
    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp < 0

class Goblin(Monster):
    def __init__(self):
        self.hp = 1
        self.attack = 1
        self.race = "Goblin"

class Orc(Monster):
    def __init__(self):
        self.hp = 2
        self.attack = 2
        self.race = "Orc"

class Troll(Monster):
    def __init__(self):
        self.hp = 5
        self.attack = 5
        self.race = "Cave Troll"

class Balrog(Monster):
    def __init__(self):
        self.hp = 10
        self.attack = 10
        self.race = "Balrog"



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
                self.monster.take_damage(self.player.attack)
                if self.monster.is_dead():
                    self.view.killed_monster_message(self.monster.race)
                    return False
                else:
                    self.view.attacked_monster_message(self.monster.race, self.player.attack)
                    self.is_players_turn = False
                    return True
            elif choice == 1:
                self.view.blocked_attack_message()
                self.is_players_turn = True
                return True
            elif choice == 2:
                able_to_flee = bool(random.getrandbits(1))
                if able_to_flee:
                    self.view.ran_away_message()
                    return False
                else:
                    self.view.couldnt_run_away_message()
                    self.is_players_turn = False
                    return True
        elif not self.is_players_turn:
            self.view.got_attacked_message(self.monster.race, self.monster.attack)
            self.player.take_damage(self.monster.attack)
            self.is_players_turn = True
            if self.player.is_dead():
                self.view.player_died_message()
                self.lost = True
                return False
            self.view.player_health_message(self.player.hp)
            return True
            #check if player is dead


game = Game()
missions = []
missions.append(Mission("Gandalf wants you to take the ring to Rivendell. What do you want to do?", ["go", "stay"], 1))
missions.append(Mission("Your party arrives in Rivendell safely. There is no consensus on what to do with the ring. Do you want to volunteer to take it to Mordor yourself?", ["yes", "no"], 2))
missions.append(Mission("Your party was unable to pass through the Misty Mountains. Which way do you want to go?", ["Moria", "The Shire"], 5))
missions.append(Mission("Fight the Balrog?", ["kick ass", "eh whatever"], 10))

game.load_missions(missions)
game.start()
game.play()