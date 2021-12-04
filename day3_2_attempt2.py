f = open("day3.txt", "r")

nums = []
for number in f:
	num = ''
	for bit in number:
		if bit != ('\n'):
			num += bit
	nums.append(num)

def oxygen_rating(values, i):
	print(values)
	if len(values) == 1:
		return values[0]
	else:
		ones = 0
		zeros = 0
		for item in values:
			if int(item[i]):
				ones += 1
			else:
				zeros += 1
		new_values = values.copy()
		if ones >= zeros:
			j = 0
			for item in values:
				j += 1
				if int(item[i]) != 1:
					new_values.remove(item)
		else:
			for item in values:
				if int(item[i]) != 0:
					new_values.remove(item)

		return oxygen_rating(new_values, i+1)

def co2_scrubber(values, i):
	print(values)
	if len(values) == 1:
		return values[0]
	else:
		ones = 0
		zeros = 0
		for item in values:
			if int(item[i]):
				ones += 1
			else:
				zeros += 1
		new_values = values.copy()
		if ones >= zeros:
			for item in values:
				if int(item[i]) == 1:
					new_values.remove(item)
		else:
			for item in values:
				if int(item[i]) == 0:
					new_values.remove(item)

		return co2_scrubber(new_values, i+1)

oxy = oxygen_rating(nums, 0)
co2 = co2_scrubber(nums, 0)

print(int(oxy, 2) * int(co2, 2))