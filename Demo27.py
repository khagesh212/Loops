# Input any 10 numbers find out first biggest and second biggest number ?

fstbig=0
secbig=0
for x in range(1,11):
    no=int(input("enter number:"))
    if fstbig>no:
        print()
    else:
        fstbig=no
    if secbig<fstbig and secbig>no:
        if fstbig==no:
            print()
        else:
            secbig=no
    else:
        secbig=no

print("First biggest number:",fstbig)
print("Second biggest number:",secbig)