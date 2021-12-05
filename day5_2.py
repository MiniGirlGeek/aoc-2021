class Line:
	max_x = 0
	max_y = 0
	def __init__(self, string):
		self.stringProcessing(string)

	def stringProcessing(self, string):
		start, end = string[:-1].split(' -> ')
		self.x1, self.y1 = [int(num) for num in start.split(",")]
		self.x2, self.y2 = [int(num) for num in end.split(",")]
		Line.max_x = max([Line.max_x, self.x1, self.x2])
		Line.max_y = max([Line.max_y, self.y1, self.y2])
		self.horizontal = (self.y1 == self.y2)
		self.vertical = (self.x1 == self.x2)

f = open("day5.txt", "r")
lines = [Line(line) for line in f]

grid = {}
for y in range(Line.max_y + 1):
	for x in range(Line.max_x + 1):
		grid[(x, y)] = 0

danger_points = set()
for line in lines:
	if line.horizontal:
		no_steps = abs(line.x2 - line.x1)
		step = (line.x2 - line.x1) // no_steps
		x = line.x1
		for i in range(no_steps + 1):
			grid[(x, line.y1)] += 1
			if grid[(x, line.y1)] >= 2:
				danger_points.add((x, line.y1))
			x += step
	elif line.vertical:
		no_steps = abs(line.y2 - line.y1)
		step = (line.y2 - line.y1) // no_steps
		y = line.y1
		for i in range(no_steps + 1):
			grid[(line.x1, y)] += 1
			if grid[(line.x1, y)] >= 2:
				danger_points.add((line.x1, y))
			y += step
	else:
		no_x_steps = abs(line.x2 - line.x1)
		x_step = (line.x2 - line.x1) // no_x_steps
		x = line.x1

		no_y_steps = abs(line.y2 - line.y1)
		y_step = (line.y2 - line.y1) // no_y_steps
		y = line.y1

		for i in range(no_x_steps + 1):
			grid[(x, y)] += 1
			if grid[(x, y)] >= 2:
				danger_points.add((x, y))
			x += x_step
			y += y_step

print(len(danger_points))

