def move(a, b):
	print(f"moving from {a} to {b}")

def hanoi(n: int, a, b, c):
	if n == 0:
		pass
	else:
		hanoi(n-1, a, c, b)
		move(a, c)
		hanoi(n-1, b, a, c)



if __name__ == "__main__":
	hanoi(5, "A", "B", "C")
