from linked_list import Node, Util

class	BinarySeach:
	total = 0
	data = {
		'Total' : [],
		'Left' : [],
		'Mid' : [],
		'Right' : []
	}
	def	__init__(self, target, arr):
		self.target = target
		self.arr = arr
	def	bns(self, left, mid, right, arr, target):
		self.total += 1
		self.data['Total'].append(self.total)
		self.data['Left'].append(left)
		self.data['Mid'].append(mid)
		self.data['Right'].append(right)
		if left > right:
			return -1, data
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid, data
		elif arr[mid] < target:
			return self.bns(mid + 1, mid, right, arr, target)
		else:
			return self.bns(left, mid, mid - 1, arr, target)

if __name__ == "__main__":
	data = [1, 2, 3, 4, 3]
	utl = Util()
	node = None
	new = None
	for i in range(len(data)):
		node = utl.add_back(node, data[i])
	# utl.print_lst(node)
	bns = BinarySeach(30, data)
	index, total = bns.bns(0, 0, len(data) - 1, data, 30)
	if (index != -1):
		print("Found at index", index, "with total", total)
	else:
		print("Not found with total", total)
	# print(bns.bns(0, 0, len(data) - 1, data, 30))
	# print("Index =", index)
	# print("Total =", total)
	# print(bns.data)
