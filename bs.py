from linked_list import Node, Util

class	BinarySeach:
	def	__init__(self, target, arr):
		self.target = target
		self.arr = arr
	def	bns(self, left, mid, right, arr, target):
		if left > right:
			return -1
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			return self.bns(mid + 1, mid, right, arr, target)
		else:
			return self.bns(left, mid, mid - 1, arr, target)

if __name__ == "__main__":
	data = [1, 2, 3, 4, 30]
	utl = Util()
	node = None
	new = None
	for i in range(len(data)):
		node = utl.add_back(node, data[i])
	# utl.print_lst(node)
	bns = BinarySeach(30, data)
	print(bns.bns(0, 0, len(data) - 1, data, 30))
