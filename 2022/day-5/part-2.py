raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

crates = [[],[],[],[],[],[],[],[],[]]
for i in range(8):
	if raw_file_contents[i][1] != ' ':
		crates[0].append(raw_file_contents[i][1])
	if raw_file_contents[i][5] != ' ':
		crates[1].append(raw_file_contents[i][5])
	if raw_file_contents[i][9] != ' ':
		crates[2].append(raw_file_contents[i][9])
	if raw_file_contents[i][13] != ' ':
		crates[3].append(raw_file_contents[i][13])
	if raw_file_contents[i][17] != ' ':
		crates[4].append(raw_file_contents[i][17])
	if raw_file_contents[i][21] != ' ':
		crates[5].append(raw_file_contents[i][21])
	if raw_file_contents[i][25] != ' ':
		crates[6].append(raw_file_contents[i][25])
	if raw_file_contents[i][29] != ' ':
		crates[7].append(raw_file_contents[i][29])
	if raw_file_contents[i][33] != ' ':
		crates[8].append(raw_file_contents[i][33])

for i in range(9):
	crates[i] = crates[i][::-1]

for i in range(10, len(raw_file_contents)):
	instruction = raw_file_contents[i].split(' ')
	
	flippadoo = []
	for i in range(int(instruction[1])):
		flippadoo.append(
			crates[int(instruction[3]) - 1].pop()
		)

	for i in range(len(flippadoo)):
		crates[int(instruction[5]) - 1].append(
				flippadoo.pop()
			)

print(f'{[x[-1] for x in crates]}')