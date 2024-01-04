base = int(input("Base: "))
expo = int(input("Exponent: "))
mod = int(input("Mod: "))


# function to find modular exponent
def bin_exp(base, exponent, mod):
    ans = 1
    while exponent:
        if exponent % 2 == 1:
            ans = (ans * base) % mod
        base = (base * base) % mod
        exponent = int(exponent) / 2
    return ans


print("Modular exponent: " + str(bin_exp(base, expo, mod)))
