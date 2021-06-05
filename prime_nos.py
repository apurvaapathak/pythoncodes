print("Prime numbers between 1 to 100 are: ")
for i in range (1, 100 +1 ):
    if(i>1):
        for x in range(2,i):
            if(i%x)==0:
                break;
        else:
            print(i)
