print("**************List Functions***************")

# *********Functions for Delete element from List***********
# del
# pop()
# remove()
# clear()

l = [10 , 20 , "Python" , 10.25 , "Programming"]
del l[2]
print(l)               # l = [10 , 20 , 10.25 , "Programming"]
print()

print(l.pop(2))        # 10.25
print(l)               # l = [10 , 20 , "Programming"]
print()

l.remove("Programming")
print(l)               # l = [10 , 20]
print()

l.clear()
print(l)               # []

print()
# *************Functions for updating elements in the List************
# insert()
# append()
# extends() 

l = [10 ,20 ,30 ,40]
l[0]=90
print(l)         # l = [90 , 20 , 30 , 40]

l.insert(3,35)
print(l)         # l = [90 , 20 , 30 , 35 , 40]
l.insert(0,25)
print(l)         # l = [25 , 90 , 20 , 30 , 35 , 40]

print()
a = [200 , 300]
l.append(a)
print(l)         # l = [25 , 90 , 20 , 30 , 35 , 40 ,[200, 300]]
l.append("Programming")
print(l)         # l = [25 , 90 , 20 , 30 , 35 , 40 , [200 , 300],'Programming']

l.extend(a)      # works on values inside the List elements
print(l)         # l = [25 , 90 , 20 , 30 , 35 , 40 ,[200 , 300],'Programming' , 200 , 300]