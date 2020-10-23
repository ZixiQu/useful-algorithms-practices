def move(a, b):
	print(f"moving from {a} to {b}")

def hanoi(n: int, a, b, c):
	if n == 0:
		pass
	else:
		hanoi(n-1, a, c, b)
		move(a, c)
		hanoi(n-1, b, a, c)


def move_tuple(a, b):
	return (a, "To" ,b)

def honoi_list(n, a, b, c) -> list:
	if n == 0:
		return []
	else:
		lst = []
		lst.extend(honoi_list(n-1, a, c, b))
		lst.append(move_tuple(a, c))
		lst.extend(honoi_list(n-1, b, a ,c))
		return lst



if __name__ == "__main__":
	# print(move_tuple("A", "B"), type(move_tuple("A", "B")))
	result = honoi_list(6, "A", "B", "C") 
	step = 1
	while result:
		thing = result.pop(0)
		print(thing, step)
		step += 1
