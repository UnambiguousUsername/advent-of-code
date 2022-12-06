raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readline()

characters_processed = 0
unique_set = {}
start_of_packet_found = 0
the_length = len(raw_file_contents)
for i in range(the_length):
	if start_of_packet_found == 0:
		unique_set.clear()
		unique_set = set({
			raw_file_contents[i],
			raw_file_contents[i + 1],
			raw_file_contents[i + 2],
			raw_file_contents[i + 3]
		})

		if len(unique_set) < 4:
			continue
		else:
			start_of_packet_found = 1
	else:
		unique_set.clear()
		unique_set = set({
			# i feel dumb pasting this, gotta be a better way
			raw_file_contents[i],
			raw_file_contents[i + 1],
			raw_file_contents[i + 2],
			raw_file_contents[i + 3],
			raw_file_contents[i + 4],
			raw_file_contents[i + 5],
			raw_file_contents[i + 6],
			raw_file_contents[i + 7],
			raw_file_contents[i + 8],
			raw_file_contents[i + 9],
			raw_file_contents[i + 10],
			raw_file_contents[i + 11],
			raw_file_contents[i + 12],
			raw_file_contents[i + 13],
		})

		if len(unique_set) < 14:
			continue
		else:
			characters_processed += i + 14
			break

print(characters_processed)