def quick_sort(lst: list) -> list:
    """ Return the sorted <lst> """
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        small = []
        big = []
        for each in lst[1:]:
            if each < pivot:
                small.append(each)
            elif each >= pivot:
                big.append(each)
        return quick_sort(small) + [pivot] + quick_sort(big)
