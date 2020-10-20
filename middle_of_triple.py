def median(a, b, c):
    """ Return the middle value of a triple using only max and min"""
    return max(min(a,b), min(max(a,b),c))
