def dec2bin(x: str):
    if x == '0':
        return "0"
    elif x == "1":
        return "1"
    mode = int(x) % 2
    rest = str(int(x) // 2)
    return dec2bin(rest) + str(mode)

if __name__ == "__main__":
    print(dec2bin("12345678"))