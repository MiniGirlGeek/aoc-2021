f = open("day2.txt", "r")

class Submarine:
	def __init__(self):
		self.depth = 0
		self.horizontal = 0
		self.aim = 0

	def forward(self, steps):
		self.horizontal += steps
		self.depth += self.aim * steps

	def down(self, steps):
		self.aim += steps

	def up(self, steps):
		self.aim -= steps

sub = Submarine()

actions = {'forward': sub.forward,
		   'up'     : sub.up,
		   'down'   : sub.down
		   }

for instruction in f:
	action, steps = instruction.split(' ')
	actions[action](int(steps))

print(f'depth: {sub.depth} horizontal: {sub.horizontal} answer: {sub.depth * sub.horizontal}')