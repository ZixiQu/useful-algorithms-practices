class random:
	name = "repr vs str"

	def __repr__(self):
		return self.name

	def __str__(self):
		return "str"


if __name__ == "__main__":
	r = random()
	