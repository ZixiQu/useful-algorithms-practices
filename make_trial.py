def make_trail(path: str):
    info = path.split()
    info = [int(i) for i in info]
    result = []
    for i in range(len(info) - 1):
        result.append(info[i])
        result.append((info[i], info[i+1]))
    result.append(info[-1])
    return result

if __name__ == "__main__":
    path = "7 1 6 2 5 3 2 7 3 4 7"
    print(make_trail(path))
