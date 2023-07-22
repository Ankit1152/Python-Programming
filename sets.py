#  Set is a collection of elemwnt which is unorderd , unindexed  that has no duplicate elements. it has unique elements

from turtle import update


my_set = {10 , 20 , 30 , 40 , 50}
print(my_set)

# Iterating sets using for loop
for a in my_set:
    print(a)

print()

# Function related to Set

# set()
# add()
# remove()
# discard()
# pop()
# clear()
# update()

l = [10,20,30,40]
s = set(l)             # set() converts into set
print(s)

my_set.remove(50)
print(my_set)

my_set.discard(40)
print(my_set)

print(my_set.pop())    # pop() randomly deletes elements in the sets
print(my_set)

my_set.add(100)
print(my_set)

my_set.update(l)       # it joins all the elements of list into the set elements
print(my_set)

my_set.clear()         # clear() returns set() method
print(my_set)