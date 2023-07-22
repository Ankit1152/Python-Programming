import numpy as np

l = [10,20,30,40]
n1 = np.array(l)
print(n1)
print(type(n1))

n2 = np.array([[1,2,3,4],[4,3,2,1]])
print(n2)


# Initializing numpy arrays with 0
n3 = np.zeros((5,5))
print(n3)


# Initializing numpy arrays with same number
n4 = np.full((5,5),10)
print(n4)


# Initializing numpy array within a range
n5 = np.arange(10,20)
print(n5)

n5 = np.arange(10,50,5)
print(n5)

n6 = np.arange(50,501)
print(n6)


# Initializing numpy array with random numbers
n7 = np.random.randint(1,100,5)
print(n7)


# Checking the shape of numpy arrays
n1 = np.array([[1,2,3,4],[4,3,2,1]])
print(n1)
print(n1.shape)

n1.shape = (4,2)
print(n1)



# Joining numpy arrays
# 1 vstack() :- vertically
n1 = np.array([10,20,30,40])
n2 = np.array([50,60,70,80])
print(np.vstack((n1,n2)))

# 2 hstack() :- horizontally
print(np.hstack((n1,n2)))

# 3 column_stack()
print(np.column_stack((n1,n2)))


# Numpy Intersection and Difference Operations
n3 = np.array([10,20,30,40,50])
n4 = np.array([40,50,60,70,80])
print(np.intersect1d(n3,n4))   # It returns the common elements from both the list

print(np.setdiff1d(n3,n4))     # It removes common elements and shows the n3 elements
print(np.setdiff1d(n4,n3))     # It removes common elements and shows the n4 elements


# Addition of Numpy Arrays
a1 = np.array([10,20])
a2 = np.array([30,40])

print(np.sum([a1,a2]))
print(np.sum([a1,a2],axis = 0))
print(np.sum([a1,a2],axis = 1))

# Basic Arithmatic Operators with numpy arrays(+,-,/,*)
a3 = np.array([10,20,30,40])
a3 = a3 + 1
print(a3)
a3 = a3 - 1
print(a3)
a3 = a3 * 2
print(a3)
a3 = a3 / 5
print(a3)


# Basic Math Function
x = np.random.randint(1,50,10)
print(x)
print(np.mean(x))
print(np.std(x))
print(np.median(x))

# Numpy save and load
print(x)
np.save('my_array',x)                       # Saving numpy array
new_numpy_arr = np.load('my_array.npy')     # Loading numpy array
print(new_numpy_arr)


