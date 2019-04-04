

class TicTacToe():
	"""docstring for TicTacToe"""
	def __init__(self):
		self.grid=[['*','*','*'],['*','*','*'],['*','*','*']]
		self.player=1
		self.win=False
    
	
	def print_game_grid(self):
		print(f'The player is {self.player}')
		for i in range(3):
			for j in range(3):
				print(self.grid[i][j]+"  ",end='')
			print()

	def gameOver(self):
		# horizontal equal

		for i in range(3) :
			if self.grid[i][0]==self.grid[i][1] and self.grid [i][1]==self.grid[i][2] and self.grid[i][0]!='*' :
				self.win=True
				return True
			return False
        
        # vertical equal 
		for i in range(3) :
			if( self.grid[0][i]==self.grid[1][i] and self.grid[1][i]==self.grid[2][i] and self.grid[0][i]!='*') :
				self.win=True
				return True
        #diagonal right
		if (self.grid[0][0]==self.grid[1][1] and self.grid[1][1]==self.grid[2][2] and self.grid[0][0]!='*'):
			self.win=True
			return True
        #diagonal left
		if (self.grid[0][2]== self.grid[1][1] and self.grid[1][1]==self.grid[2][0] and self.grid[0][2]!='*'):
			self.win=True
			return True

		#none left to fill 
		full= '*' in grid[0] or '*' in grid[1] or '*' in grid[2]

		if full:
			return False


	def ask_user_for_position(self):
		print("Which position would you choose next")
		try:
			r=int(input("enter the row"))
			c=int(input("enter the column"))

			if(self.player==1):
				self.grid[r][c]='X'
			else:
				self.grid[r][c]='O'
		except:
			print("invalid row / column number ")
			self.ask_user_for_position()
		self.player_take_chance()

	def player_take_chance(self):
		if(self.player==1):
			self.player=2
		else:
			self.player=1

	def start_game(self):
		while not self.gameOver():
			self.ask_user_for_position()
			self.print_game_grid()
		if(self.win):
			if self.player==1:
				print("Player 2 won !")
			else :print("Player 1 won!")
		else:
			print("nobody won !! \n Game was a draw")
		

			

ticTac = TicTacToe()
ticTac.start_game()