raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

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
				
				for i in range(1, len(coords)):
					if abs(coords[i][1] - coords[i - 1][1]) > 1:
						coords[i][1] += 1
						coords[i][0] = coords[i - 1][0]
						tail_set.add(tuple(coords[-1][:]))
		case 'R':
			for _ in range(steps):
				coords[0][0] += 1
				for i in range(1, len(coords)):
					if abs(coords[i][0] - coords[i - 1][0]) > 1:
						coords[i][0] += 1
						coords[i][1] = coords[i - 1][1]
						tail_set.add(tuple(coords[-1][:]))
		case 'D':
			for _ in range(steps):
				coords[0][1] -= 1
				for i in range(1, len(coords)):
					if abs(coords[i][1] - coords[i - 1][1]) > 1:
						coords[i][1] -= 1
						coords[i][0] = coords[i - 1][0]
						tail_set.add(tuple(coords[-1][:]))
		case 'L':
			for _ in range(steps):
				coords[0][0] -= 1
				for i in range(1, len(coords)):
					if abs(coords[i][0] - coords[i - 1][0]) > 1:
						coords[i][0] -= 1
						coords[i][1] = coords[i - 1][1]
						tail_set.add(tuple(coords[-1][:]))

print(len(tail_set))