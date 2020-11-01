def median(a, b, c):
    """ Return the middle value of a triple using only max and min"""
    return max(min(a,b), min(max(a,b),c))


if __name__ == "__main__":
    print(median(5,3,8))
