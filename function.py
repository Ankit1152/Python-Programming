# Simple function
def showdata():
	print("Welcome to Python programming")

showdata()
showdata()
showdata()

# Function with arguement

def sum(a,b):
	print(a+b)

sum(10,20)
sum(50,60)

# Function with default value

def sum(a,b=10):
	print(a+b)

sum(20)
sum(20,50)

# Function with return statement 
def square(x):
    return x*x , x*2

s = square(5)
print(s)
