# Find the factorial of a given number ?

no=int(input("Enter a number:"))
fact=1
for i in range(no,0,-1):
    fact=fact*i
print("Factorial of",no,"is",fact)