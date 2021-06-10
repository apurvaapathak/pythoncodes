print("**********Welcome to Supermarket!!!**********")

a = ['coke', 'oats', 'berries', 'curd', 'chips']

s = input("Which item do you want to buy?")

x = s.lower()
print(x)

for i in a:
    if i == x:
        a.remove(i)
        print("The left items in the list are: ")
        print(a)
