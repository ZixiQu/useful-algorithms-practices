from __future__ import annotations

class BST:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def __str__(self):
		if not self.left and not self.right:
			return str(self.value)

		result = f"{self.left.__str__() if self.left else None} -> {self.value} -> {self.right.__str__() if self.right else None}"
		return result

	def __eq__(self, other: BST):
		if type(other) != BST:
			raise TypeError(f"{type(other)} is not BST type")
		return self.value == other.value

	def minimum(self):
		if not self.left:
			return self.value
		return self.left.minimum()

	def maximum(self):
		if not self.right:
			return self.value
		return self.right.maximum()

	def search(self, value):
		if value == self.value:
			return True
		if not self.left and not self.right:
			return False
		if value < self.value:
			return self.left.search(value)
		if value > self.value:
			return self.right.search(value)

	def successor(self):
		if self.right:
			return self.right.minimum()
		return self._successor_helper()

	def _successor_helper(self):
		if not self.parent:
			return None
		if self.parent.left is self:
			return self.parent
		return self.parent._successor_helper()

	def predecessor(self):
		pass




if __name__ == "__main__":
	b = BST(2)
	b.left = BST(0, BST(-1, parent=b.left), BST(1, parent=b.left), b)
	b.right = BST(4, BST(3, parent=b.right), BST(5, parent=b.right), b)


	b.left.left.parent = b.left
	b.left.right.parent = b.left
	b.right.left.parent = b.right
	b.right.right.parent = b.right
	

	print(b)
	suc1 = b.successor()
	subtree2 = b.right.right
	suc2 = subtree2.successor()
	print(suc2)

	
	