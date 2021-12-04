f = open("day3.txt", "r")

transpose = [[],[],[],[],[]]
#transpose = [[],[],[],[],[],[],[],[],[],[],[],[]]

nums = []
oxygen_gen = []
co2_scrub = []

for number in f:
	i = 0
	num = ''
	for bit in number:
		if bit != ('\n'):
			num += bit
			transpose[i].append(int(bit))
		i += 1
	nums.append(num)
	oxygen_gen.append(num)
	co2_scrub.append(num)

gamma = ''
epsilon = ''

for row in transpose:
	if sum(row) > (len(row)/2):
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'


i = 0
for char in gamma:
	for num in nums:
		if num[i] != char:
			if (num in oxygen_gen) and len(oxygen_gen) > 1:
				oxygen_gen.remove(num)
		else:
			if (num in co2_scrub) and len(co2_scrub) > 1:
				co2_scrub.remove(num)
	i += 1

print(oxygen_gen[0], co2_scrub[0])
print(int(oxygen_gen[0], 2) * int(co2_scrub[0], 2))

