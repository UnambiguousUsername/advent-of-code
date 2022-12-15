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

		
		for u in range(h - 1, 0, -1):
			next_tree = raw_file_contents[u][w]
			if len(up) == 0:
				up.append(next_tree)
			elif next_tree > up[-1]:
				up.append(next_tree)
			
			if up[-1] >= raw_file_contents[h][w]:
				break

		for r in range(w + 1, width):
			next_tree = raw_file_contents[h][r]
			if len(right) == 0:
				right.append(next_tree)
			elif next_tree > right[-1]:
				right.append(next_tree)

			if right[-1] >= raw_file_contents[h][w]:
				break

		for d in range(h + 1, height):
			next_tree = raw_file_contents[d][w]
			if len(down) == 0:
				down.append(next_tree)
			elif next_tree > down[-1]:
				down.append(next_tree)

			if down[-1] >= raw_file_contents[h][w]:
				break

		for l in range(w - 1, 0, -1):
			next_tree = raw_file_contents[h][l]
			if len(left) == 0:
				left.append(next_tree)
			elif next_tree > left[-1]:
				left.append(next_tree)

			if left[-1] >= raw_file_contents[h][w]:
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