end = int(input("How many terms you want to print? "))

def fib(e):
    f1 = 0
    f2 = 1
    t = 0
    while t < e:
        print(f1)
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        t += 1

fib(end)
