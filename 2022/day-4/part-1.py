raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

contained_count = 0
for line in raw_file_contents:
	pairs = line.strip()
	pairs = pairs.split(',')
	elf1 = pairs[0].split('-')
	elf2 = pairs[1].split('-')

	if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
			contained_count += 1
	elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
			contained_count += 1

print(contained_count)