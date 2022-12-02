raw_file_contents = []
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

elf_counter = 0
elf_calorie_amounts = []
elf_calorie_amounts.append(0)
for line in raw_file_contents:
	if line.isspace():
		elf_counter += 1
		elf_calorie_amounts.append(0)
	else:
		elf_calorie_amounts[elf_counter] += int(line)

elf_calorie_amounts.sort()

print(
	elf_calorie_amounts[-1]
	+ elf_calorie_amounts[-2]
	+ elf_calorie_amounts[-3]
	)