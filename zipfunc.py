# Using zip() function to iterate more than one lists at the same time
print("*********Using Zip function**********")

l = [10,20,30,40]
l1 = [50,60,70,80] 
for a,b in zip(l,l1):
    print(a,b)

l2 = [58,85,45,67,74]
for a,b,c in zip(l,l1,l2):
    print(a,b,c)

print("*********Without zip function************")
t = len(l)

for h in range(t):
    print(l[h],l1[h],l2[h])