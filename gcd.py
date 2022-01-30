def gcd(a, b):
    """ Return the greatest common devider(gcd) between a and b using
    Euclidean Algorithm with recursion

    pre: a and b are integeres 1 <= b <= a  (edit 2021.9.30, the comparison of a and b doesn't matter. b > a is fine)
    post: returns the greatest common divisor of a and b
    """
    if a == 1 and b == 1:
        return 1
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def U(n):
    """ U(n) = {[a] in Z_n: gcd(a,n) = 1}
    
    >>> U(10)
    [1, 3, 7, 9]
    >>> U(12)
    [1, 5, 7, 11]
    """
    result = []
    for each in range(1, n):
        if gcd(each, n) == 1:
            result.append(each)

    return result


if __name__ == "__main__":
    print(gcd(17,101))
    # print(U(10))

    # print(U(10))