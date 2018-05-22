

import random
from rpg_view_MVC import View
import sys


# What is the best way to store and iterate through missions?
## What is the best way to dock player health points?


class Game_Controller:
    """ Begin game, compile missions, create player """

    def __init__(self):

        self.missions = ['mission_one', 'mission_two']
        self.mission_index = 0
        self.player = None
        self.view = View()
        self.random = Randomizer()


    def start_game(self):
        """ edit self.player using create_player """
        self.player = self.create_player()


    def create_player(self):
        """ run through sequence of events """

        name = self.view.input_player_name()
        race = self.view.input_player_race()
        self.view.introduction_message()
        self.view.dinner_decision()
        self.view.dinner_message()
        self.view.mission_choice_message()
        self.view.money_message("50")
        self.view.money_decision()
        self.view.attacker_message(self.random.make_random_antagonist())
        self.view.attack_message(self.random.make_random_attack())
        self.view.make_battle_decision()
        self.view.choose_battle_menuever()
        # self.player.health_damaged()
        # return Player(name, race)


    def play(self):
        """ run through list of missions until completed """

        self.create_player()
        while self.mission_index < len(self.missions):
            # self.view.passed_mission_message()
            self.mission_index += 1


    def load_missions(self, missions):
        """ add additional missions """

        self.missions = missions
        self.mission_index = 0



class Player:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.health = 10
        self.attack = 2
        print (self.name, self.race, self.health, self.attack)

    def health_damaged(self, damage):
        self.health -= damage
        print (self.health)

    def died(self):
        return self.health <=0



class Randomizer:
    """ randomly select antogonist and attack type """

    def make_random_antagonist(cls):
        level = random.randint(1,4)
        if level == 1:
            antagonist = "priest"
        if level == 2:
            antagonist = "teenager"
        if level == 3:
            antagonist = "grandmother"
        if level == 4:
            antagonist = "jogger"
        return antagonist

    def make_random_attack(cls):
        level = random.randint(1,4)
        if level == 1:
            attack = "your toe stepped on"
        if level == 2:
            attack = "spat upon"
        if level == 3:
            attack = "bumped really hard"
        if level == 4:
            attack = "poked in the eye"
        return attack



class Antagonist:
    def health_damaged(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp < 0

class teenage(Antagonist):
    def __init__(self):
        self.hp = 1
        self.attack = 1
        self.race = "teenager"

class grandmother(Antagonist):
    def __init__(self):
        self.hp = 2
        self.attack = 2
        self.race = "grandmother"

class jogger(Antagonist):
    def __init__(self):
        self.hp = 5
        self.attack = 5
        self.race = "jogger"



game = Game_Controller()
game.play()





