class Bingo:
	def __init__(self, string):
		self.grid = self.stringToGrid(string)
		self.unmarked = self.stringToGrid(string)
		self.rows = [0, 0, 0, 0, 0]
		self.cols = [0, 0, 0, 0, 0]
		self.bingo = False

	def stringToGrid(self, string):
		grid = []
		for row in string.split('\n'):
			new_row = []
			for char in row.split(' '):
				if char != '':
					new_row.append(int(char))
			grid.append(new_row)
		return grid

	def checkFor(self,called_num):
		y = 0
		for row in self.grid:
			x = 0
			for num in row:
				if num == called_num:
					self.unmarked[y][x] = 0
					self.rows[y] += 1
					self.cols[x] += 1
					if self.rows[y] == 5 or self.cols[x] == 5:
						self.bingo = True
				x += 1
			y += 1
		return self.bingo

	def totalUnmarked(self):
		return sum([sum(row) for row in self.unmarked])

f = open("day4.txt", "r")
f_string = f.read()
f_data = f_string.split('\n\n')

bingo_nums = [int(num) for num in f_data[0].split(',')]
bingo_grids = [Bingo(string) for string in f_data[1:]]
found = False

for num in bingo_nums:
	if found:
		break
	for grid in bingo_grids:
		if found:
			break
		if grid.checkFor(num):
			print(grid.totalUnmarked() * num)
			found = True