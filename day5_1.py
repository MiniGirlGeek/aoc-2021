class Line:
	max_x = 0
	max_y = 0
	def __init__(self, string):
		self.stringProcessing(string)

	def stringProcessing(self, string):
		start, end = string[:-1].split(' -> ')
		x1, y1 = [int(num) for num in start.split(",")]
		x2, y2 = [int(num) for num in end.split(",")]
		Line.max_x = max([Line.max_x, x1, x2])
		Line.max_y = max([Line.max_y, y1, y2])
		self.horizontal = (y1 == y2)
		self.vertical = (x1 == x2)

		self.x1 = min([x1, x2])
		self.x2 = max([x1, x2])
		self.y1 = min([y1, y2])
		self.y2 = max([y1, y2])

f = open("day5.txt", "r")
lines = [Line(line) for line in f]

grid = {}
for y in range(Line.max_y + 1):
	for x in range(Line.max_x + 1):
		grid[(x, y)] = 0

danger_points = set()
for line in lines:
	if line.horizontal:
		for x in range(line.x1, line.x2 + 1):
			grid[(x, line.y1)] += 1
			if grid[(x, line.y1)] >= 2:
				danger_points.add((x, line.y1))
	if line.vertical:
		for y in range(line.y1, line.y2 + 1):
			grid[(line.x1, y)] += 1
			if grid[(line.x1, y)] >= 2:
				danger_points.add((line.x1, y))

print(danger_points)
print(len(danger_points))

