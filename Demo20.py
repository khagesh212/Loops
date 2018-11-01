# Print sum of all even numbers from 1 to 10 numbers ?

sum=0
for x in range(1,11):
    if x%2==0:
        sum=sum+x
print("Sum of even numbers:",sum)