raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readline()

characters_processed = 0
the_length = len(raw_file_contents)
for i in range(the_length):
	unique_set = set({
		raw_file_contents[i],
		raw_file_contents[i + 1],
		raw_file_contents[i + 2],
		raw_file_contents[i + 3]
	})

	if len(unique_set) < 4:
		continue
	else:
		characters_processed = i + 4
		break

print(characters_processed)