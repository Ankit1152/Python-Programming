#    0    1    2     3       4            5
l = [10, 20 , 30 ,"Hello", 10.25 , [25 , 26 , 41]]
#   -6  -5   -4     -3      -2           -1

print(l[2] , l[3] , l[5] , l[5][2] , l[-1][-2])

# Slicing the list elements
print("**************Slicing the list elements**************")

print("list elements is",l[0:6])
print("First three list elements is",l[0:3])
print(l[0::2])
print(l[0::3])

# Reverse Slicing
print("Reverse of List elements : ",l[-1::-1])
print(l[-1::-2])
print(l[-3::-1])
print(l[-1:-4:-1])

# List Iteration
print("************1st way of List Iteration************")
l = [10 , 20 , "hello" , 10.25 , [10,20]]
t = len(l)

for x in range(t):
    print(l[x])

print("************2nd way of List iteration************")  

for x in l:
    print(x)

print("*************Reverse iteration of List elements************")

for x in range(t-1,-1,-1):
    print(l[x])

