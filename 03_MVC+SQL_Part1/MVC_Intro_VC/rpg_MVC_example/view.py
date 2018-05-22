class View:
    def __init__(self):
        pass

    def input_player_name(self):
        while True:
            name = input("Enter your character's name: ")
            if name != "":
                break
        return name

    def input_player_race(self):
        while True:
            race = input("Enter your race [elf, dwarf, wizard]: ")
            if race in ["elf","dwarf","wizard"]:               
                break
        return race

    def introduction_message(self):
        print("INTRODUCTION: Welcome to the game. You mus destroy the ring!")


    def passed_mission_message(self):
        print("Success! You passed the mission!")

    def failed_mission_message(self):
        print("You let Sauron destroy the world. Oops!")
    
    def input_mission_decision(self, actions):
        while True:
            decision = input("Choose your destiny! [{}] or [{}]: ".format(actions[0], actions[1]))
            if decision in actions:
                break
        return decision 

    def mission_description(self, description):
        print(description)
   
    def battle_decision(self):
        choice = ""
        while True:
            choice = input("Attack [0], Shield [1], Flee [2]: ")
            if choice in ["0","1","2"]:
                break
        return int(choice)

    def killed_monster_message(self, race):
        print("You killed the {}!".format(race))

    def attacked_monster_message(self, race, damage):
        print("You attacked the {}! It took {} damage!".format(race, damage))

    def got_attacked_message(self, race, damage):
        print("You got attacked by the {}! You took {} damage!".format(race, damage))
    def blocked_attack_message(self):
        print("You blocked a hit!")

    def ran_away_message(self):
        print("You ran away!")

    def couldnt_run_away_message(self):
        print("Couldn't run away!")

    def player_died_message(self):
        print("You Died!")

    def player_health_message(self, hp):
        print("Health left: {}".format(hp))