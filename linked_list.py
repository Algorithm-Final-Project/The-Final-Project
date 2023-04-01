class	Node:
	i = 0
	def	__init__(self, data):
		Node.i += 1
		self.data = data
		self.next = None
		self.id = Node.i

class	Util:
	def	add_back(self, lst : Node, data):
		if lst == None:
			return Node(data)
		else:
			lst.next = self.add_back(lst.next, data)
			return lst

	def	print_lst(self, lst : Node):
		if lst == None:
			return
		else:
			print("Data =", lst.data)
			print("ID =", lst.id)
			self.print_lst(lst.next)

# if __name__ == "__main__":
# 	data = [1, 2, 3]
# 	i = 0
# 	utl = Util()
# 	lst = None
# 	for i in range(len(data)):
# 		new = Node(data[i])
# 		lst = utl.add_back(lst, new.data)
