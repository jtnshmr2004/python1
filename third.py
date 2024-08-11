# wap to find out whether a student has passed or failed if it require a total of 40% and atleast 33% in each subject
marks_1=int(input("enter marks of first subject: "))
marks_2=int(input("enter marks of second subject: "))
marks_3=int(input("enter marks of third subject: "))

total_percentage = (100 *(marks_1+marks_2+marks_3))/100
if(total_percentage>40 and marks_1>33 and marks_2>33 and marks_3>33):
    print("student is pass" ,total_percentage)
else:
    print("student is fail",total_percentage)