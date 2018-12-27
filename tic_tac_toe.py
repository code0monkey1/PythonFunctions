

class TicTacToe():
	"""docstring for TicTacToe"""
	def __init__(self):
		super(TicTacToe, self).__init__()
		self.grid=[['*','*','*'],['*','*','*'],['*','*','*']]
		self.player=1

    
	
	def print_game_grid(self):
		for i in range(3):
			for j in range(3):
				print(self.grid[i][j]+"  ",end='')
			print()

	def gameOver(self):
		# horizontal equal

		for i in range(3) :
			if self.grid[i][0]==self.grid[i][1] and self.grid [i][1]==self.grid[i][2] and self.grid[i][0]!='*' :
				return True
			return False
        
        # vertical equal 
		for i in range(3) :
			if( self.grid[0][i]==self.grid[1][i] and self.grid[1][i]==self.grid[2][i]) :
				return true
        #diagonal right
		if (self.grid[0][0]==self.grid[1][1] and self.grid[1][1]==self.grid[2][2]):
			return true
        #diagonal left
		if (self.grid[0][2]== self.grid[1][1] and self.grid[1][1]==self.grid[2][0]):
			return true

		#none left to fill 
		all_full = True
		for i in range(3):
			for j in range(3):
				if(self.grid[i][j]=='*'):
					all_full=False

		if all_full:
			return True


	def ask_user_for_position(self):
		print("Which position would you choose next")
		try:
			r=input("enter the row")
			c=input("enter the column")

			if(player==1):
				self.grid[r][c]='X'
			else:
				self.grid[r][c]='O'
		except:
			print("invalid row / column number ")
			ask_user_for_position()

	def player_take_chance(self):
		if(player==1):
			player=2
		else:
			player=1

	def start_game(self):
		while not self.gameOver():
			self.ask_user_for_position()
			self.print_game_grid()

			

ticTac = TicTacToe()
ticTac.start_game()