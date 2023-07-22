n = input("Enter the value of the string:")
print(n)
print("List :",(n.split()))    # USing split() func to convert into list

#  Using for loop to convert into list 

l = []
for a in range(1,4):
    n = input("Enter the string "+str(a)+":-")
    l.append(n)

print(l)    