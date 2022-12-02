HAND_SCORES = {
	'A X': 3,
	'A Y': 4,
	'A Z': 8,
	'B X': 1,
	'B Y': 5,
	'B Z': 9,
	'C X': 2,
	'C Y': 6,
	'C Z': 7 
}

def round_results(combatants):
	combatants = combatants.rstrip()

	return HAND_SCORES[combatants]

raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

sum = 0
for line in raw_file_contents:
	sum += round_results(line)

print(sum)