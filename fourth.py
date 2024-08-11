# check spam comments
p1="make a lot of money"
p2="subscribe now"
p3="buy this"
p4="click on this link"
message=input("enter your comment :")
if(p1 in message or p2 in message or p3 in message):
    print("this comment is a spam")
else:
    print("this comment is not a spam")