raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

def move_the_rope(coords_list):
	for i in range(1, len(coords)):
		if abs(coords_list[i][0] - coords_list[i - 1][0]) > 1 and abs(coords_list[i][1] - coords_list[i - 1][1]) > 1:
			coords_list[i][0]  += ((coords_list[i - 1][0] - coords_list[i][0]) / 2)
			coords_list[i][1]  += ((coords_list[i - 1][1] - coords_list[i][1]) / 2)
		elif abs(coords_list[i][0] - coords_list[i - 1][0]) > 1:
			coords_list[i][0]  += ((coords_list[i - 1][0] - coords_list[i][0]) / 2)
			coords_list[i][1] = coords_list[i - 1][1]
		elif abs(coords_list[i][1] - coords_list[i - 1][1]) > 1:
			coords_list[i][1]  += ((coords_list[i - 1][1] - coords_list[i][1]) / 2)
			coords_list[i][0] = coords_list[i - 1][0]
		else:
			pass

coords = [[0, 0] for _ in range(10)]
tail_set = set()
tail_set.add((0, 0))

for line in raw_file_contents:
	direction, steps = line.rstrip().split(' ')
	steps = int(steps)
	
	match direction:
		case 'U':
			for _ in range(steps):
				coords[0][1] += 1
				move_the_rope(coords)
				tail_set.add(tuple(coords[-1][:]))
		case 'R':
			for _ in range(steps):
				coords[0][0] += 1
				move_the_rope(coords)
				tail_set.add(tuple(coords[-1][:]))
		case 'D':
			for _ in range(steps):
				coords[0][1] -= 1
				move_the_rope(coords)
				tail_set.add(tuple(coords[-1][:]))
		case 'L':
			for _ in range(steps):
				coords[0][0] -= 1
				move_the_rope(coords)
				tail_set.add(tuple(coords[-1][:]))

print(len(tail_set))