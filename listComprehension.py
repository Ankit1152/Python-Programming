# Normal way to create or append elements in the list

l = []

for a in range(1 , 101):
    l.append(a)

print(l)

print()
# Using List Comprehension to append elements in the lists 

newlist = [m for m in range(1 , 101) if m%2==0]
print(newlist)

print()

s = 'Programming'
d = [g for g in s]
print(d)