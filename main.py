import numpy as np
from random import randint
import time

class Game():
	Matrix = np.zeros((4,4),dtype = np.int)
	#Matrix = [[0 for x in range(4)] for y in range(4)] 
 
	def __init__(self):
		print("help")
		for col in range(0,4):	
			for i in range(0,4):
				self.Matrix[i][col] = 0


	def print_mat(self):
		print(np.matrix(self.Matrix))


	def add_a_value(self):
		print("amount of nonzeros:", np.count_nonzero(self.Matrix)+1)
		if (np.count_nonzero(self.Matrix) == 16):
			return -1
		
		r = randint(0,3)
		c = randint(0,3)
		num = 2*randint(1,2)
		#optimise it
		while(self.Matrix[r][c] != 0): #something buggy
			r = randint(0,3)
			c = randint(0,3)
		
		self.Matrix[r][c] = num
		#self.print_mat()
		return 1
	
	def swipe_down(self):
		for col in range(0,4):	
			for i in range(3,0,-1):
				if self.Matrix[i][col] == self.Matrix[i-1][col]:
					self.Matrix[i][col] = 2*self.Matrix[i][col]
					self.Matrix[i-1][col] = 0
					self.move_zeroes_down()	

		#self.print_mat()

	def move_zeroes_down(self):
		i = 3
		j = 0
		col = 0
		while col!=4:
			i = 3
			
			while i!=-1:
				j = i
				if self.Matrix[j][col] == 0:
					while self.Matrix[j][col]==0:
						if j!=0:
							j = j -1
						else: break
					self.Matrix[i][col] = self.Matrix[j][col]
					self.Matrix[j][col] = 0
					#print(i,j)
				#print(self.Matrix)
				i = i-1
			col = col+1

	def swipe_up(self):
		self.Matrix = self.Matrix[::-1]
		#print(self.Matrix)
		self.swipe_down()
		self.Matrix = self.Matrix[::-1]
		#print(self.Matrix)

	
	def swipe_left(self):
		#self.print_mat()
		#print("swiping left..")
		for row in range(0,4):	
			for i in range(3,0,-1):
				if self.Matrix[row][i] == self.Matrix[row][i-1]:
					self.Matrix[row][i] = 2*self.Matrix[row][i]
					self.Matrix[row][i-1] = 0
					self.move_zeroes_left()	
		#self.print_mat()			

	def move_zeroes_left(self):
		i = 3
		j = 0
		row = 0
		while row!=4:
			i = 0
			while i!=4:
				j = i
				if self.Matrix[row][j] == 0:
					while self.Matrix[row][j]==0:
						if j!=3:
							j = j + 1
						else: break
					self.Matrix[row][i] = self.Matrix[row][j]
					self.Matrix[row][j] = 0
					#print(i,j)
				#print(self.Matrix)
				i = i+1
			row = row+1

	def swipe_right(self):
		self.Matrix = np.fliplr(self.Matrix)
		#print(self.Matrix)
		self.swipe_left()
		self.Matrix = np.fliplr(self.Matrix)
		#print(self.Matrix)

	

instance1 = Game()
#instance1.print_mat()
instance1.add_a_value()
a = 5

while (True):
	instance1.print_mat()
	asa = input()
	a = int(asa)
	if (a == 2):
		print("down..")
		instance1.swipe_down()
		instance1.add_a_value()
	elif (a == 8):
		print("up..")
		instance1.swipe_up()
		instance1.add_a_value()
	elif (a == 4):
		print("left..")
		instance1.swipe_left()
		instance1.add_a_value()
	elif (a == 6):
		print("right..")
		instance1.swipe_right()
		instance1.add_a_value()
	else:
		instance1.print_mat() 
