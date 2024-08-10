# WAP to find greatest of four number entered by user
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
d=int(input("enter value of d:"))
if(a>b and a>c and a>d):
    print("a is greatest",a) 
elif(b>a and b>c and b>d):
    print("b is greatest",b) 
elif(c>b and c>a and c>d):
    print("c is greatest",c) 
else:
    print("d is greatest ",d) 

