def gcd(a, b):
    """ Return the greatest common devider(gcd) between a and b using
    Euclidean Algorithm with recursion

    pre: a and b are integeres 1 <= b <= a
    post: returns the greatest common divisor of a and b
    """
    if a == 1 and b == 1:
        return 1
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(30, 216))