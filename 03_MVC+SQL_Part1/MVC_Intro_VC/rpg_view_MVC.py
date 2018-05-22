

import sys


class View:

    def input_player_name(self):
        while True:
            name = input("\n\n\n\n\nHi. What's your character's name?")
            if name != "":
                print ("\nNice to meet you, %s.\n" % (name))
                break
        return name


    def input_player_race(self):
        while True:
            race = input("\nWhat is your character's occupation?\n 1) aspiring artist,\n 2) low-level drug dealer,\n 3) under-performing sales rep\n")
            if race in ["1","2","3"]:
                break
        return race
        

    def introduction_message(self):
        print ("\nOkay. Get ready for a wild ride.\n")
        

    def dinner_decision(self):
        print ("\nWhat would you like for dinner?")
        choice = ""
        while True:
            choice = input("\n1) microwaved burrito,\n2) microwaved corndog,\n3) microwaved pizza.\n")
            if choice in ["1","2","3"]:
                break
        return int(choice)
        

    def dinner_message(self):
        print("Whatever. You're the boss.")
        print("\nYikes. That wasn't such a good decision.")
        print ("\nHEALTH DEDUCTION OF 2 POINTS! \n")
        

    def mission_choice_message(self):
        print ("\nSo, where would you like to go tonight?")
        while True:
            choice = input("\n1) the bingo hall,\n2) to recycle some bottles for change,\n3) a bodega to buy a lotto ticket and cheetos.\n ")
            if choice in ["1","2","3"]:
                print ("\nOkay. It's your life after all.\n")
                break
        return int(choice)


    def money_message(self, dollars_won):
        print("\nWhoa! You just won %s dollars! You are so lucky!!!\n" % (dollars_won))
        print("\nLIFE IS GOOD!\n")
        

    def money_decision(self):
        print ("\nThis is really exciting. What would you like to do with your newfound riches?")
        while True:
            choice = input("\n1) put it towards that overdue parking ticket,\n2) buy a case of beer,\n3) consider investing in crypto.\n ")
            if choice in ["1","2","3"]:
                print ("\nGreat decision. Onward and upward!\n")
                break
        return int(choice)


    def attacker_message(self, attacker):
        print("\nUh oh. Looks like there is a menacing looking %s approaching...\n" %(attacker))
        

    def attack_message(self, attack):
        print("\nOh no! You just got %s!\n" %(attack))
        
        print("HOW RUDE!\n")
        

    def make_battle_decision(self):
        print ("\nDo you want to fight back?\n")
        while True:
            choice = input("\n1) of course,\n2) nope.\n ")
            if choice == "1":
                
                print ("\nGreat. Now's the chance to get out some of that pent up rage.\n")
                break

            else:
                print("Good decision. Just bottle up that rage and save it for later.")
                
                self.failed_mission_message()
                sys.exit()
        
        return int(choice)


    def choose_battle_menuever(self):
        print ("\nHow do you want to fight back?")
        choice = ""
        while True:
            choice = input("\n1) jab with your keys,\n2) pull hair,\n3) bite.\n ")
            if choice in ["1", "2", "3"]:
                self.successful_mission_message()
                break
        return int(choice)


    def failed_mission_message(self):
        print("\nBummer. Now you're in a bad mood. I guess you' weren't 'so lucky after all.\n")
        print("\nTHE END")


    def successful_mission_message(self):
        print("\nWow. That was pretty embarassing. I guess you weren't so lucky after all.\n")
        print("\nTHE END")

    


