raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

print(raw_file_contents[1].strip().split(' '))