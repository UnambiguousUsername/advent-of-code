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

max_calories = 0
for elf in elf_calorie_amounts:
	if elf > max_calories:
		max_calories = elf

print(max_calories)