lower=int(input("Enter starting value:"))
higher=int(input("Enter ending value:"))

for i in range(lower,higher+1):
    if i>1:
        for num in range(2,i):
            if(i%num)==0:
                break
        else:
           print(i)