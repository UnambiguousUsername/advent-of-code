HAND_SCORES = {
	'A X': 4,
	'A Y': 8,
	'A Z': 3,
	'B X': 1,
	'B Y': 5,
	'B Z': 9,
	'C X': 7,
	'C Y': 2,
	'C Z': 6
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