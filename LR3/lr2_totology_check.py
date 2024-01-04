# this code is to check if a simple and/or logic with 2 variables is a tautology or not
cnt = 0
a = input()  # taking input string
a = a.replace(" ", "")
# spliting input into variables depending on the logic
if "|" in a:
    b, c = map(str, a.split("|"))
elif "&" in a:
    b, c = map(str, a.split("&"))

l1 = [True, False]
l2 = [True, False]
result = False

if "-" in b:
    l1 = [False, True]
if "-" in c:
    l2 = [False, True]


def checkTauto(a, b, c):  # function to check tautolog
    global cnt
    if "|" in a:
        if b or c:
            result = True
        else:
            result = False
            cnt += 1  # if false for any case, returns cnt > 0
    if "&" in a:
        if b and c:
            result = True
        else:
            result = False
            cnt += 1
    print("=> " + str(result))  # to print the truth table


def diffVar(a, b, c):
    # to tassign bool values to variables if they are different
    for i in l1:
        for j in l2:
            print(i, j)
            b = i
            c = j
            checkTauto(a, b, c)
    if cnt > 0:
        print("Not tautology")
    else:
        print("Is Tautology")


def sameVar(a, b, c):  # to tassign bool values to variables if they are same
    for i in l1:
        for j in l2:
            if b == c:  # if vars are same bool can't be different
                if i != j:
                    continue
            if b != c:  # if vars are same but inverse, bool can't be same
                if i == j:
                    continue
            print(i, j)
            b = i
            c = j
            checkTauto(a, b, c)
    if cnt > 0:  # if cnt>0 at least 1 case is false
        print("Not tautology")
    else:
        print("Is Tautology")


if b not in c:
    diffVar(a, b, c)
else:
    sameVar(a, b, c)
