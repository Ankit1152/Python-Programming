print("Arithematic Operators")

a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b**2) #Exponents
print(a//b) #Floor divisions or returns integer value

print("Assignment Operators")

x = 5
print(x)

x = x + 5
print(x)
x += 5
print(x)

x = x - 5
print(x)
x -= 5
print(x)

x *= 2
print(x)

x /= 2
print(x)

print("Comparison Operators")

x = 10
y = 20

print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

print("Logical Operators")

x = 10
y = 20

print(x==10 and x<=y)
print(x<=y or x>=y)
print(not x!=y)

print("Membership Operators")

string = "Hello"
print('h' in string)
print('H' in string)

l = [10 , 20 , 60 , 50, 40]
print(10 in l)
print(30 in l)
print(30 not in l)

print('Identity Operators')

x = 10
y = 10
print(x is y)        # it is similar to x==y
print(x is not y)    # it is similar to x!=y


print('Bitwise Operators')

x = 10
y = 8

print(bin(x))          # 0b1010
print(bin(y))          # 0b1000  
print(bin(x&y) , x&y)  # 0b1000  8
print(bin(x|y) , x|y)  # 0b1010  10
print(bin(x^y) , x^y)  # 0b10    2

