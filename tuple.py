
t = (10,20,30,40,50,10)

a = t[2]
print(a)

print()

# Iterating tuple using for loop
l = len(t)
for x in range(l):
    print(t[x])

print()

# Iterating tuple directly pass the tuple
for x in t:
    print(x)

print()

# Functions related to Tuples
# min()
# max()
# sum()
# index()
# count()

a = min(t)
print(a)

b = max(t)
print(b)

c = t.count(10)
print(c)

d = t.index(30)
print(d)

e = sum(t)
print(e)

f = sum(t,20)
print(f)