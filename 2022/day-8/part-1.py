raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

hidden_trees = 0
height = len(raw_file_contents)

for q in range(height):
	raw_file_contents[q] = raw_file_contents[q].rstrip()

width = len(raw_file_contents[0])
cant_be_seen_matrix = [[0] * width for i in range(height)]

# left to right
for i in range(height):
	max_height = None
	for j in range(width):
		current_tree = raw_file_contents[i][j]
		if max_height is None:
			max_height = current_tree
		elif current_tree < max_height:
			cant_be_seen_matrix[i][j] = 1
		else:
			max_height = current_tree

# right to left
for i in range(height):
	max_height = None
	for j in range(width):
		current_tree = raw_file_contents[i][-j]
		if max_height is None:
			max_height = current_tree
			if cant_be_seen_matrix[i][-j] == 1:
				cant_be_seen_matrix[i][-j] = 0
		elif current_tree >= max_height:
			max_height = current_tree
			if cant_be_seen_matrix[i][-j] == 1:
				cant_be_seen_matrix[i][-j] = 0

# up to down
for i in range(height):
	max_height = None
	for j in range(width):
		current_tree = raw_file_contents[j][i]
		if max_height is None:
			max_height = current_tree
			if cant_be_seen_matrix[j][i] == 1:
				cant_be_seen_matrix[j][i] = 0
		elif current_tree >= max_height:
			max_height = current_tree
			if cant_be_seen_matrix[j][i] == 1:
				cant_be_seen_matrix[j][i] = 0

# down to up
for i in range(height):
	max_height = None
	for j in range(width):
		current_tree = raw_file_contents[j][-i]
		if max_height is None:
			max_height = current_tree
			if cant_be_seen_matrix[j][-i] == 1:
				cant_be_seen_matrix[j][-i] = 0
		elif current_tree >= max_height:
			max_height = current_tree
			if cant_be_seen_matrix[j][-i] == 1:
				cant_be_seen_matrix[j][-i] = 0

hidden_trees = 0
for i in range(height):
	for j in range(width):
		if cant_be_seen_matrix[i][j] == 1:
			hidden_trees += 1

print(hidden_trees)