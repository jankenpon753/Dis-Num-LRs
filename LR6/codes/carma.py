# finding GCD
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


# finding modular exponent
def modExpo(x, y, mod):
    if y == 0:
        return 1
    temp = modExpo(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


# function to find Carmichael number
def carmaNumber(n):
    b = 2
    while b < n:
        if gcd(b, n) == 1:
            if modExpo(b, n - 1, n) != 1:
                return 0
        b = b + 1
    return 1


for i in range(0, 5):
    x = int(input())
    if carmaNumber(x):
        print(str(x) + " is Carmichael")
    else:
        print(str(x) + " is NOT Carmichael")
