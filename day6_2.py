f = open("day6.txt", "r")

state = [int(num) for num in f.readlines()[0].split(',')]
days = 256

fish_states = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}

total_fish = 0
for fish in state:
	fish_states[fish] += 1
	total_fish += 1


for day in range(days):
	new_fish_states = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}
	for state in fish_states.keys():
		if state != 0:
			new_fish_states[state-1] = fish_states[state]
		else:
			new_fish_states[8] = fish_states[state]
			new_fish_states[6] += fish_states[state]
			total_fish += fish_states[state]
			
	fish_states = new_fish_states

print(total_fish)