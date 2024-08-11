# wap to print multiplication table of n usinf for loops in reverse order
n=int(input("enter the number :"))
for i in range(1,11):
    print(f"{n} * {11 - i} = {n*(11-i)}")
    i=i-1
