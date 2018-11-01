# Write a program to check the number is prime or not ?

def prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

no=int(input("Enter a number:"))
if prime(no):
    print(no,"is prime number")
else:
    print(no,"is not a prime number")


