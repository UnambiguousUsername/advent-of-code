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
			if len(up) == 0:
				up.append(u)
			elif u >= current_tree:
				up.append(u)
				break
			elif u >= up[-1]:
				up.append(u)

		if w < width - 1:
			for r in list(raw_file_contents[h][w + 1:]):
				if len(right) == 0:
					right.append(r)
				elif r >= current_tree:
					right.append(r)
					break
				elif r >= right[-1]:
					right.append(r)

		if h < height - 1:
			for d in list([line[w] for line in raw_file_contents[h + 1:]]):
				if len(down) == 0:
					down.append(d)
				elif d >= current_tree:
					down.append(d)
					break
				elif d >= down[-1]:
					down.append(d)

		for l in list(raw_file_contents[h][:w])[::-1]:
			if len(left) == 0:
				left.append(l)
			elif l >= current_tree:
				left.append(l)
				break
			elif l >= left[-1]:
				left.append(l)

		scenic_score = (
			len(up)
			* len(right)
			* len(down)
			* len(left)
		)
		if scenic_score > best_scenic_score:
			best_scenic_score = scenic_score

print(best_scenic_score)