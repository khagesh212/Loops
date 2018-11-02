# Input any 10 numbers find out number of positive numbers and number of negative numbers ?

pos=0
neg=0
for x in range(10):
    no = int(input("Enter numbers:"))
    if no>0:
        pos+=1
    else:
        neg+=1
print("Number of positive numbers:",pos)
print("Number of negative numbers:",neg)