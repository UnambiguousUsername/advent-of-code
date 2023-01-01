class Monkey:

	def __init__(self, input_list):
		for i in range(len(input_list)):
			input_list[i] = input_list[i].strip().split(' ')
		
		self.items = [int(''.join(x[:-1])) for x in input_list[0] if x[-1] == ',']
		self.items.append(int(input_list[0][-1]))
		self.operation = [input_list[1][-2], input_list[1][-1]]
		self.test_divisor = int(input_list[2][-1])
		self.business_associates = [int(input_list[3][-1]), int(input_list[4][-1])]
		self.inspection_count = 0

	def inspect_items(self):
		for i in range(len(self.items)):
			self.inspection_count += 1
			match self.operation[0]:
				case '+':
					self.items[i] += self.items[i] if self.operation[1] == 'old' else int(self.operation[1])
				case '-':
					self.items[i] -= self.items[i] if self.operation[1] == 'old' else int(self.operation[1])
				case '*':
					self.items[i] *= self.items[i] if self.operation[1] == 'old' else int(self.operation[1])
				case '/':
					self.items[i] /= self.items[i] if self.operation[1] == 'old' else int(self.operation[1])
			self.items[i] = int(self.items[i] / 3)
			
	def throw_items(self, monkey_list):
		self.items = self.items[::1]
		for i in range(len(self.items)):
			current_item = self.items.pop()
			if current_item % self.test_divisor == 0:
				monkey_list[self.business_associates[0]].add_item(current_item)
			else:
				monkey_list[self.business_associates[1]].add_item(current_item)
	
	def add_item(self, item):
		self.items.append(item)

	def get_inspection_count(self):
		return self.inspection_count

	def get_item_list(self):
		return self.items

raw_file_contents = ''
with open('input.txt', 'rt') as input:
	raw_file_contents = input.readlines()

monkeys = []

for i, line in enumerate(raw_file_contents):
	if line[0] == 'M':
		monkeys.append(Monkey(raw_file_contents[i + 1:i + 6]))

for i in range(20):
	for monkey in monkeys:
		monkey.inspect_items()
		monkey.throw_items(monkeys)

inspect_count_list = [monkey.get_inspection_count() for monkey in monkeys]

inspect_count_list.sort()

print(inspect_count_list[-1] * inspect_count_list[-2])