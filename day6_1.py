f = open("day6.txt", "r")

state = [int(num) for num in f.readlines()[0].split(',')]
days = 256

for day in range(days):
	new_fish = 0
	new_state = []
	for fish in state:
		if fish == 0:
			new_fish += 1
			new_state.append(6)
		else:
			new_state.append(fish - 1)
	new_state += [8 for fish in range(new_fish)]
	state = new_state
print(len(state))
