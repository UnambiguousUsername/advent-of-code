raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

height_radius = 0
width_radius = 0
current_hr = 0
current_wr = 0
for line in raw_file_contents:
	direction, steps = line.rstrip().split(' ')
