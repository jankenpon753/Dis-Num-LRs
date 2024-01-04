# importing the previuosly defined dunctions from other files
from amodularExpo import bin_exp
from bbinaryAddSub import bin_add, bin_sub

base = int(input("Base: "))
expo = int(input("Exponent: "))
mod = int(input("Mod: "))
a = input("Binary A: ")
b = input("Binary B: ")
# using the functions directly
print("Modular exponent: " + str(bin_exp(base, expo, mod)))
print("Sum of A & B = " + bin_add(a, b))
print("Difference of A & B = " + bin_sub(a, b))
