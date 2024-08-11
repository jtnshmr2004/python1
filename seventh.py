# # wap to  write multiplication table of a number
# n = int(input("enter a number whose table is to be written"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# with while loop 
i=1
n = int(input("enter a number whose table is to be written"))

while(i<11):
    print(f"{n} * {i} = {n*i}")
    i+=1