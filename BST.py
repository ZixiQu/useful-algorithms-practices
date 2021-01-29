class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		if not self.left and not self.right:
			return str(self.value)
		result = ""
		if self.left:
			result += self.left.__str__() + " -> "
		
		result += str(self.value) + " -> "
		
		if self.right:
			result += self.right.__str__() + " -> "
		return result.strip(" -> ")

	def __repr__(self):
		return self.value
		
class BST:
	def __init__(self):
		self.root = None

	def __str__(self):
		return self.root.__str__()

	def search(self, value) -> bool:
		if self.root.value == value:
			return True
		if not self.root.left and not self.root.right:
			return False
		if value < self.root.value:
			return self.left.search(value)
		if value > self.root.value:
			return self.right.search(value)


if __name__ == "__main__":
	bst = BST()

	bst.root = Node(2, Node(1, Node(0), Node(1.5)), Node(3))
	print(bst.search(1.1))