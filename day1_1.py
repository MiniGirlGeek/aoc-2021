f = open("day1_1.txt", "r")

prev = False
no_increases = 0
for number in f:
	number = int(number)
	if prev:
		if number > prev:
			no_increases += 1
	prev = number

print(no_increases)