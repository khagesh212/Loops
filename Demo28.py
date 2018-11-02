# Input any 10 numbers find out number of prime numbers ?

prime=0
for x in range(10):
    no = int(input("Enter numbers:"))
    for y in range(2,no//2+1):
        if no<2 and no%x==0:
            break
        else:
            prime+=1
print("Number of prime numbers:",prime)