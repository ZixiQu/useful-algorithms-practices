def karatsuba(num1, num2):
    num1Str, num2Str = str(num1), str(num2)

    if num1Str[0] == '-': return -karatsuba(-num1, num2)
    if num2Str[0] == '-': return -karatsuba(num1, -num2)

    if num1 < 10 or num2 < 10: return num1 * num2
    
    maxLength = max(len(num1Str), len(num2Str))
    num1Str = ''.join(list('0' * maxLength)[:-len(num1Str)] + list(num1Str))
    num2Str = ''.join(list('0' * maxLength)[:-len(num2Str)] + list(num2Str))
    
    splitPosition = maxLength // 2
    high1, low1 = int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    high2, low2 = int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])
    z0, z2 = karatsuba(low1, low2), karatsuba(high1, high2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    return z2 * 10 ** (2 * splitPosition) + (z1 - z2 - z0) * 10 ** (splitPosition) + z0


print(karatsuba(123123123123123123123123,12321312321321321321321312))