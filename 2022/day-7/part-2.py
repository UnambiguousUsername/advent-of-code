import time

class file_system:
	def __init__(self, **kwargs):
		self.name = (
			kwargs['name'] if 'name' in kwargs else 'UNKNOWN'
		)
		self.parent_directory = (
			kwargs['parent'] if 'parent' in kwargs else None
		)
		self.child_directories = []
		self.child_files = []
		self.disk_size = 0

	def __str__(self):
		return self.name

	def add_child_directory(self, elternteil, kind):
		self.child_directories.append(file_system(parent=elternteil, name=kind))
	def add_child_file(self, file):
		self.child_files.append(file)

	def calculate_disk_size(self):
		size = 0
		size += sum([int(x[0]) for x in self.child_files])
		for child in self.child_directories:
			size += child.get_disk_size()
		self.disk_size = size

	def get_child_directory(self, kind):
		for child in self.child_directories:
			if child.get_name() == kind:
				return child
		return None
	def get_disk_size(self):
		return self.disk_size
	def get_name(self):
		return self.name
	def get_parent_directory(self):
		return self.parent_directory

	def traverse(self, size_array = []):
		if self.child_directories:
			for child in self.child_directories:
				child.traverse(size_array)
		self.calculate_disk_size()
		size_array.append(self.disk_size)
		return size_array

raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

root_node = file_system(name='/')
current_node = root_node
for line in raw_file_contents:
	line_parts = line.rstrip().split(' ')

	if line_parts[1] == 'cd' and line_parts[0] == '$':
		if line_parts[2] == '/':
			continue
		elif line_parts[2] == '..':
			current_node = current_node.get_parent_directory()
		else:
			current_node = current_node.get_child_directory(line_parts[2])
	elif line_parts[0] == 'dir':
		current_node.add_child_directory(current_node, line_parts[1])
	elif line_parts[0].isnumeric():
		current_node.add_child_file(line_parts)
	else:
		continue


all_sizes = [x for x in root_node.traverse()]
root_size = root_node.get_disk_size()
to_free_up = 30000000 - (70000000 - root_size)
big_dirs = [x for x in all_sizes if x >= to_free_up]
big_dirs.sort()

print(big_dirs[0])