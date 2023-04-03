import os
from art import *

class	BinarySeach:
	total = 0
	data = {
		'Total' : [],
		'Left' : [],
		'Mid' : [],
		'Right' : []
	}
	def	__init__(self):
		pass
	def	bns(self, left, mid, right, arr, target):
		self.total += 1
		self.data['Left'].append(left)
		self.data['Mid'].append(mid)
		self.data['Right'].append(right)
		if left > right:
			self.data['Total'] = self.total
			return -1, self.data
		mid = (left + right) // 2
		if arr[mid] == target:
			self.data['Total'] = self.total
			return mid, self.data
		elif arr[mid] < target:
			return self.bns(mid + 1, mid, right, arr, target)
		else:
			return self.bns(left, mid, mid - 1, arr, target)
	def	check_sort(self, arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i + 1]:
				return False
		return True
	def	check_num(self, arr):
		for i in arr:
			if i.isnumeric() == False:
				return False
		return True
	def	bye(self):
		tprint("Thank you")
		exit()

if __name__ == "__main__":
	tprint("Binary", font = "block")
	tprint("Search", font = "block")
	os.system("sleep 5")
	os.system("clear")
	bn = BinarySeach()
	a = input("Enter Input : ").split(",")
	if (bn.check_num(a) == False):
		print("Not Number")
		os.system("sleep 3")
		bn.bye()
		exit()
	if (bn.check_sort(a) == False):
		print("Not Sorted")
		os.system("sleep 3")
		bn.bye()
		exit()
	b = input("Enter Target : ")
	os.system("clear")
	index, data = bn.bns(0, 0, len(a) - 1, a, b)
	if index == -1:
		tprint("Not Found")
		os.system("sleep 3")
		bn.bye()
		exit()
	else:
		print("Found at index", index)
		print("Total", data['Total'], "times")
		count = 0
		for left, mid, right in zip(data['Left'], data['Mid'], data['Right']):
			count += 1
			print("Round", count, ":", end = " ")
			print("Left =", left, "Mid =", mid, "Right =", right)