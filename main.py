from player import Player
from slotmachine import SlotMachine

import utils
from database import Database

if __name__ == "__main__":
    utils.clearscreen()

    player_nickname = utils.read("What's your nickname? ")

    database = Database()

    player = database.lookfor(player_nickname)

    if player is None:  # We create a new account
        player = Player(player_nickname)

    utils.write(f"Welcome to <Casino Simulator>, {player.get_nickname()}! A world of bets awaits you!")

    slotmachine = SlotMachine(player)
