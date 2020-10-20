def free_time(c1, c2, time):
    biglist = []
    biglist.extend(c1)
    biglist.extend(c2)
    result = []

    # selection sort implementing sorting biglist
    while biglist:
        smallest = None
        time_slot = []
        for each in biglist:
            if smallest == None or compare(smallest, each[0]) == 1:
                smallest = each[0]
                time_slot = each
        result.append(time_slot)
        biglist.remove(time_slot)
    newlist = []
    while result:
        if len(result) == 1:
            newlist.append(result.pop())
        else:
            first = result.pop(0)
            second = result.pop(0)
            if compare(first[1], second[1]) == 1:
                newlist.append(first)
            elif compare(first[1], second[0]) == 1:
                newlist.append([first[0], second[1]])
            else:
                newlist.append(first)
                result.insert(0, second)
    final = []
    for i in range(len(newlist) - 1):
        if timedif(newlist[i][1], newlist[i + 1][0]) > time:
            final.append([newlist[i][1], newlist[i + 1][0]])
    return final
    

def compare(time1, time2):
    """
    time: "12:00"
    return -1 if time 1 is earlier than time2
    """
    hour1, minute1 = time1.split(":")
    hour2, minute2 = time2.split(":")
    hour1, hour2, minute1, minute2 = \
           int(hour1), int(hour2), int(minute1), int(minute2)
    if (hour1 * 60 + minute1) < (hour2 * 60 + minute2):
        return -1
    elif (hour1 * 60 + minute1) == (hour2 * 60 + minute2):
        return 0
    return 1


def timedif(time1, time2):
    hour1, minute1 = time1.split(":")
    hour2, minute2 = time2.split(":")
    hour1, hour2, minute1, minute2 = \
           int(hour1), int(hour2), int(minute1), int(minute2)
    return (hour2 * 60 + minute2) - (hour1 * 60 + minute1) 
