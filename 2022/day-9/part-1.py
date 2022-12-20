raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

tail_set = set([0,0])
h_coords = [0,0]
t_coords = [0,0]
for line in raw_file_contents:
	direction, steps = line.rstrip().split(' ')

	match direction:
		case 'U':
			
		case 'R':
			pass
		case 'D':
			pass
		case 'L':
			pass