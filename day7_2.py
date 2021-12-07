import math
f = open("day7.txt", "r")

crabs = [int(crab) for crab in f.readline().split(',')]
max_crab_pos = max(crabs)
min_fuel_cost = math.inf

def fuel(n):
	return (n*(n+1))//2

for i in range(max_crab_pos + 1):
	fuel_cost = sum([fuel(abs(i - pos)) * crabs.count(pos) for pos in range(max_crab_pos + 1)])
	min_fuel_cost = min(min_fuel_cost, fuel_cost)

print(min_fuel_cost)