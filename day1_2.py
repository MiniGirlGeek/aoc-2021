f = open("day1_1.txt", "r")

prev_wind = [False, False, False]
curr_wind = [False, False, False]
no_increases = 0

for number in f:
	number = int(number)
	curr_wind = curr_wind[1:] + [number]
	if False not in prev_wind:
		if sum(curr_wind) > sum(prev_wind):
			no_increases += 1
	prev_wind = curr_wind


print(no_increases)