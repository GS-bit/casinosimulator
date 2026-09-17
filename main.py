from player import Player
from slotmachine import SlotMachine

import utils

if __name__ == "__main__":
    utils.clearscreen()

    player = Player(utils.read("What's your name? "))

    utils.write(f"Welcome to <Casino Simulator>, {player.name}! A world of bets awaits you!")

    slotmachine = SlotMachine(player)
