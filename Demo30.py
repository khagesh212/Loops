# Input any 4 digit number and find out the sum of the digits?

sum=0
num=int(input("Enter a Number:"))
if (num>999 and num<10000):
    while num != 0:
        r = num % 10
        num = num // 10
        sum += r
    print("The Reverse Number:", sum)
else:
    print("Enter 4 digit number")

