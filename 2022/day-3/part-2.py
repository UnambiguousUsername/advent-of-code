raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

sum_of_priorities = 0
group_of_sacks = []
damn_im_so_bad_i_had_to_make_this_counter = 1

for i in range(len(raw_file_contents)):
	group_of_sacks.append(raw_file_contents[i].rstrip())

	if damn_im_so_bad_i_had_to_make_this_counter % 3 == 0:
		common_dict = {}
		local_dict = {}

		for letter in group_of_sacks[0]:
			if local_dict.get(letter, 0) == 0:
				common_dict[letter] = common_dict.get(letter, 0) + 1
				local_dict[letter] = 1
		
		local_dict.clear()
		for letter in group_of_sacks[1]:
			if local_dict.get(letter, 0) == 0:
				common_dict[letter] = common_dict.get(letter, 0) + 1
				local_dict[letter] = 1
		
		local_dict.clear()
		for letter in group_of_sacks[2]:
			if local_dict.get(letter, 0) == 0:
				common_dict[letter] = common_dict.get(letter, 0) + 1
				local_dict[letter] = 1

		for a, (b, c) in enumerate(common_dict.items()):
			if c == 3:
				if ord(b) > 95:
					sum_of_priorities += ord(b) - 96
				else:
					sum_of_priorities += ord(b) - 38

		local_dict.clear()
		common_dict.clear()
		group_of_sacks.clear()

	if damn_im_so_bad_i_had_to_make_this_counter == 3:
		damn_im_so_bad_i_had_to_make_this_counter = 1
	else:
		damn_im_so_bad_i_had_to_make_this_counter += 1
	
print(sum_of_priorities)