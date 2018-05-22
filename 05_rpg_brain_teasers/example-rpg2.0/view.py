class View:
    def __init__(self):
        pass

    def quit_game(self, player):
        print("Your progress has been saved. See you next time {}!\n".format(player.username))


    def login_or_register(self):
        while True:
            print("Login [0]")
            print("Register [1]")
            choice = input("What do you want to do?: ")
            if choice in ["0","1"]:
                break
        return int(choice)

    def login_incorrect_message(self):
        print("The username or password you entered was incorrect!\n")

    def input_username(self):
        while True:
            name = input("Enter you user name (NOT YOUR CHARACTER NAME): ")
            if name != "":
                break
        return name

    def input_password(self):
        while True:
            name = input("Enter your password: ")
            if name != "":
                break
        return name

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

    def room_description(self, room):
        print("\n{}".format(room.description))

    def input_room_decision(self, actions):
        while True:
            decision = input("Which way do you want to go now? Possible actions are: {}: ".format(actions))
            if decision in actions:
                break
        return decision 

    def wrong_way_message(self, direction):
        print("\nYou can't move {}! Choose another direction.".format(direction))

    def welcome_message(self):
        print("Welcome to \"THE MYSTERY OF THE ROBOT NINJA\"!\n")


    def passed_mission_message(self):
        print("Wow! You handled that well....\n")

    def failed_mission_message(self):
        print("You failed!\n")
    
    def input_mission_decision(self, actions):
        while True:
            decision = input("Choose your destiny! [{}] or [{}]: ".format(actions[0], actions[1]))
            if decision in actions:
                break
        return decision 

    def mission_description(self, description):
        print(description)

    def battle_started_message(self, race):
        print("That was the only logical choice. Oh snap-- a {} just jumped out in front of you!\n".format(race))
    
    def battle_decision(self):
        choice = ""
        while True:
            choice = input("Attack [0], Shield [1], Flee [2]: ")
            if choice in ["0","1","2"]:
                break
        return int(choice)

    def killed_monster_message(self, monster, player):
        print("You killed the {}!".format(monster.race))
        print("You earned {} EXP!".format(monster.exp))
        print("You now have {} EXP!".format(player.exp))

    def attacked_monster_message(self, race, damage):
        print("You attacked the {}! It took {} damage!\n".format(race, damage))

    def got_attacked_message(self, race, damage):
        print("You got attacked by the {}! You took {} damage!\n".format(race, damage))
    def blocked_attack_message(self):
        print("You blocked a hit!\n")

    def ran_away_message(self):
        print("You ran away!\n")

    def couldnt_run_away_message(self):
        print("Couldn't run away!\n")

    def player_died_message(self):
        print("You Died!\n")

    def player_health_message(self, hp):
        print("Health left: {}".format(hp))
