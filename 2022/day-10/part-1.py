raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

raw_file_contents = raw_file_contents[::-1]
register = 1
signal_strength = 0
instruction_time = 0

for i in range(1, 221):
	if instruction_time == 0:
		current_instruction = raw_file_contents.pop().rstrip().split(' ')
		if len(current_instruction) > 1:
			instruction_time += 1
			current_instruction[1] = int(current_instruction[1])
	else:
		instruction_time -= 1

	if (i / 20 < 12) and ((i / 20) % 2 == 1):
		signal_strength += register * i
	
	if len(current_instruction) > 1 and instruction_time == 0:
		register += current_instruction[1]

print(signal_strength)