from array import *

arr = array('i', [1,2,3,4,5,6])
print(arr)

print(arr[2])

for i in arr:
    print(i)

print(arr.buffer_info())

for i in range(5):
    print(arr[i])

for i in range(1,4):
    print(i, arr[i])


arr.reverse()
print(arr)

arr.append(10)
print(arr)

arr.remove(5)
print(arr)


# Input the array elements
arr = array('i', [])
size = int(input("Enter the size of the array :"))
for i in range(size):
    n = int(input())
    arr.append(n)

print(arr)


