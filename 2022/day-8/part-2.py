raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

height = len(raw_file_contents)
for q in range(height):
	raw_file_contents[q] = raw_file_contents[q].rstrip()
width = len(raw_file_contents[0])

best_scenic_score = 0
for h in range(height):
	for w in range(width):
		up = []
		right = []
		down = []
		left = []
		current_tree = raw_file_contents[h][w]

		for u in list([line[w] for line in raw_file_contents[:h]])[::-1]:
			up.append(u)
			if u >= current_tree:
				break

		if w < width - 1:
			for r in list(raw_file_contents[h][w + 1:]):
				right.append(r)
				if r >= current_tree:
					break

		if h < height - 1:
			for d in list([line[w] for line in raw_file_contents[h + 1:]]):
				down.append(d)
				if d >= current_tree:
					break

		for l in list(raw_file_contents[h][:w])[::-1]:
			left.append(l)
			if l >= current_tree:
				break

		scenic_score = (
			len(up)
			* len(right)
			* len(down)
			* len(left)
		)
		if scenic_score > best_scenic_score:
			best_scenic_score = scenic_score

print(best_scenic_score)