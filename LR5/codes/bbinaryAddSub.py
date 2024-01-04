a = input("Binary A: ")
b = input("Binary B: ")

# bionary addition function
def bin_add(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ""
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == "1" else 0
        r += 1 if b[i] == "1" else 0
        result = ("1" if r % 2 == 1 else "0") + result
        # carry
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = "1" + result
    return result.zfill(max_len)


# subtraction function, useing 2's compliment
def bin_sub(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    ch = ""

    c = compliment(b)
    result = bin_add(a, c)

    if len(result) > max_len:
        if result[0] == "1":
            compliment(result)
            for i in range(1, len(result)):
                ch += result[i]
        return ch
    else:
        return result


# finding 2's compliment of binary number
def compliment(a):
    newa = ""
    for i in range(0, len(a)):
        if a[i] == "1":
            newa += "0"
        else:
            newa += "1"
    return bin_add(newa, "1")


print("Sum of A & B = " + bin_add(a, b))
print("Difference of A & B = " + bin_sub(a, b))
