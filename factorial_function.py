a = int(input("Enter the number for which you want to find factorial: "))


def factoriall(numb):
    f = 1
    for x in range(1, numb + 1):
        f = f * x
    print(f"The factorial of {numb} is {f}")


factoriall(a)
