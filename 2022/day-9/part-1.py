raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

h_coords = [0,0]
t_coords = [0,0]
tail_set = set()
tail_set.add((0, 0))

for line in raw_file_contents:
	direction, steps = line.rstrip().split(' ')
	steps = int(steps)

	match direction:
		case 'U':
			for _ in range(steps):
				h_coords[1] += 1
				if abs(h_coords[1] - t_coords[1]) > 1:
					t_coords[1] += 1
					t_coords[0] = h_coords[0]
					tail_set.add(tuple(t_coords[:]))
		case 'R':
			for _ in range(steps):
				h_coords[0] += 1
				if abs(h_coords[0] - t_coords[0]) > 1:
					t_coords[0] += 1
					t_coords[1] = h_coords[1]
					tail_set.add(tuple(t_coords[:]))
		case 'D':
			for _ in range(steps):
				h_coords[1] -= 1
				if abs(h_coords[1] - t_coords[1]) > 1:
					t_coords[1] -= 1
					t_coords[0] = h_coords[0]
					tail_set.add(tuple(t_coords[:]))
		case 'L':
			for _ in range(steps):
				h_coords[0] -= 1
				if abs(h_coords[0] - t_coords[0]) > 1:
					t_coords[0] -= 1
					t_coords[1] = h_coords[1]
					tail_set.add(tuple(t_coords[:]))

print(len(tail_set))