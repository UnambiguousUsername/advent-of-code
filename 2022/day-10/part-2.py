raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

raw_file_contents = raw_file_contents[::-1]
register = 1
signal_strength = 0
instruction_time = 0
graphics = [' ' for _ in range(240)]

for i in range(len(graphics)):
	if instruction_time == 0:
		current_instruction = raw_file_contents.pop().rstrip().split(' ')
		if len(current_instruction) > 1:
			instruction_time += 1
			current_instruction[1] = int(current_instruction[1])
	else:
		instruction_time -= 1

	if abs((i % 40) - register) < 2:
		graphics[i] = '#'
	
	if len(current_instruction) > 1 and instruction_time == 0:
		register += current_instruction[1]

graphics = ''.join(graphics)

for i in range(6):
	print(f'{graphics[i * 40:(i + 1) * 40]}')