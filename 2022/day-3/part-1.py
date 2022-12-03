raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

sum_of_priorities = 0
for line in raw_file_contents:
	n = len(line.rstrip())
	first_half = line[0:n//2]
	second_half = line[n//2:]

	commonality = ''

	for letter in first_half:
		if letter in second_half:
			commonality = letter
			break
	
	if ord(commonality) > 95:
		sum_of_priorities += ord(commonality) - 96
	else:
		sum_of_priorities += ord(commonality) - 38

print(sum_of_priorities)