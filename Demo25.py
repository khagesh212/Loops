# Input any 10 numbers find out number of even numbers and number of odd numbers ?

even=0
odd=0
for x in range(10):
    no = int(input("Enter numbers:"))
    if no%2==0:
        even+=1
    else:
        odd+=1
print("Number of even no:",even)
print("Number of odd no:",odd)