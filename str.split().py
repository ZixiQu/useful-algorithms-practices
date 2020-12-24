def split(s: str, sep=" \n\t"):
    """ simimulating python str.split()"""
    # print(sep)
    result = [""]
    for each in s:
        if not each in sep:
            result[-1] += each
        elif each in sep and result[-1] != "":
            result.append("")
    return result

if __name__ == "__main__":
    print(split("something, hello, world", sep=","))

