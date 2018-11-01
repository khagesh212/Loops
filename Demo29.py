# Input any 4 digit number and reverse it ?

num=int(input("Enter a Number:"))
rev=0
if num>999 and num<10000:
    while num!=0:
        r=num%10
        num=num//10
        rev=(rev*10)+r
    print("The Reverse Number:",rev)
else:
    print("Enter 4 digit number")

