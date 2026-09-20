import random
import time

import utils
from database import Database

class SlotMachine:
    """
    This class represents the slot machine.
    """

    def __init__(self, player):
        self.slot1 = None  # First slot
        self.slot2 = None  # Second slot
        self.slot3 = None  # Third slot

        # Symbols used in the slot machine:
        self.symbols = [{"name": "CHERRY", "probability": 28.5, "multiplier": 1.5}, 
                        {"name": "ORANGE", "probability": 23.8, "multiplier": 2}, 
                        {"name": "GRAPE", "probability": 19.0, "multiplier": 3},
                        {"name": "DIAMOND", "probability": 14.3, "multiplier": 5},
                        {"name": "BELL", "probability": 9.5, "multiplier": 8},
                        {"name": "7", "probability": 4.8, "multiplier": 15}]

        self.player = player  # We need to connect the slot machine to our player, so we can make the bets possible.

        self.database = Database()  # Data to save during the game

        self.gameloop()

    def gameloop(self) -> None:
        """
        Slot machine loop.
        """
        
        playing = True

        while self.player.get_money() > 0 and playing:
            utils.write(f"|| You have: {self.player.get_money_with_symbol()} ||")

            utils.write("What to do?")
            op = utils.menu(["BET", "LEAVE"])
            
            match op:
                case 1:
                    self.play(utils.read("How much to bet? (type only a positive integer): ", "UINT"))
                case 2:
                    playing = False

                    utils.write("See you later! =]")
                case _:
                    utils.write("Invalid operation!")

        if self.player.get_money() == 0:
            utils.write("Game over, you have no money now =[")

    def play(self, bet: int) -> None:
        """
        It rolls the slot machine, showing the movement on the screen and updating the player's money.

        Arguments:
            bet: player's bet
        """

        if self.player.can_bet(bet):
            result = random.choices([symbol["name"] for symbol in self.symbols], weights=[symbol["probability"] for symbol in self.symbols], k=3)

            utils.clearscreen()

            utils.write("Rolling...")

            time.sleep(1)

            for i in range(3):
                utils.write(f"Slot{i+1} = {result[i]}")
            
                time.sleep(1)

            if result[0] == result[1] == result[2]:
                # Looking for the symbol multiplier:
                for symbol in self.symbols:
                    if symbol["name"] == result[0]:
                        multiplier = symbol["multiplier"]
                        break

                to_receive = int(self.player.get_money()*multiplier - self.player.get_money())

                self.player.receive_money(to_receive)
                utils.write("+simu$ " + str(to_receive) + "!")
            elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
                multiplier = 1

                # Looking for the symbol multiplier:
                for symbol in self.symbols:
                    if symbol["name"] == result[0] and symbol["name"] == result[1]:
                        multiplier = symbol["multiplier"]
                        break
                    elif symbol["name"] == result[1] and symbol["name"] == result[2]:
                        multiplier = symbol["multiplier"]
                        break
                    elif symbol["name"] == result[0] and symbol["name"] == result[2]:
                        multiplier = symbol["multiplier"]
                        break

                to_receive = int((self.player.get_money()*multiplier - self.player.get_money()) / 3)

                self.player.receive_money(to_receive)
                utils.write("You got simu$ " + str(to_receive) + "!")
            else:
                self.player.lose_money(bet)
                utils.write("You lost simu$ " + str(bet) + "!")

            self.database.save_players_data(self.player)
        else:
            utils.write(f"Sorry, you can't bet simu$ {bet}, for you don't have this amount...")
