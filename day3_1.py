f = open("day3.txt", "r")

#transpose = [[],[],[],[],[]]
transpose = [[],[],[],[],[],[],[],[],[],[],[],[]]

for number in f:
	i = 0
	for bit in number:
		if bit != ('\n'):
			transpose[i].append(int(bit))
		i += 1

gamma = ''
epsilon = ''

for row in transpose:
	if sum(row) > (len(row)/2):
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

print(gamma, int(gamma, 2), epsilon, int(epsilon, 2), int(gamma, 2) * int(epsilon, 2))