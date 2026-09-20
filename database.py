import sqlite3

from player import Player

class Database:
	"""
	This class represents the database.
	"""

	def __init__(self):
		self.conn = sqlite3.connect('gamedata.db')  # Database connection
		self.cursor = self.conn.cursor()  # Cursor

		# We will use a table that contains all players of the casino:
		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS players (
					nickname TEXT NOT NULL UNIQUE,
					money INTEGER NOT NULL
				);
			""")

		self.conn.commit()
	
	def lookfor(self, nickname: str) -> Player:
		"""
		It looks for the passed nickname in the database.

		If the nickname is present, then the function returns a Player object with the player's information.
		Otherwise, the function returns None.
		"""

		self.cursor.execute(
			"""SELECT nickname, money FROM players
			WHERE nickname = ?; 
			""", (nickname,))

		result = self.cursor.fetchone()

		if result:
			return Player(result[0], result[1])

		return None

	def save_players_data(self, player: Player) -> int:
		"""
		It saves the player's data into the database.

		Arguments:
			player: the player object

		Return:
			False if it was successful, True otherwise.
		"""

		try:
			self.cursor.execute(
				"""UPDATE players
				SET money = ?
				WHERE nickname = ?;
				""", (player.get_money(), player.get_nickname()))

			if self.cursor.rowcount == 0:
				self.cursor.execute(
				""" INSERT INTO players
				VALUES (?, ?);
				""", (player.get_nickname(), player.get_money()))

			self.conn.commit()

			return 0
		except Exception as e:
			self.conn.rollback()

			return 1
	
	def __del__(self):
		self.conn.close()	
