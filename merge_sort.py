def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    first = merge_sort(lst[:mid])
    second = merge_sort(lst[mid:])

    return merge(first, second)


def merge_slow(lst1, lst2):
    """ This implement is O(n^2) implement. High Readibility.
    n = len(lst1) + len(lst2)
    """
    result = []
    while lst1 and lst2:  # O(n)
        if lst1[0] <= lst2[0]:
            result.append(lst1.pop(0))  # (n^2)
        else:
            result.append(lst2.pop(0))
    if len(lst1) != 0:
        result.extend(lst1)
    if len(lst2) != 0:
        result.extend(lst2)

    return result

def merge(lst1, lst2):
    """ This implementation is O(n) runtime. Good algorithm.
    n = len(lst1) + len(lst2)
    """
    result = []
    index1, index2 = 0, 0

    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            result.append(lst1[index1])
            index1 += 1
        else:
            result.append(lst2[index2])
            index2 += 1

    result.extend(lst1[index1:])
    result.extend(lst2[index2:])

    return result

if __name__ == "__main__":
    lst = [6,5,4,1,2,3]  # input the data here
    print(merge_sort(lst))