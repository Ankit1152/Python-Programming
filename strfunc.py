# Strings functions
print("*************Strings Functions in Python**************")

# lower()
# upper()
# title()
# capitalize()

str = "WELCOME TO PYTHON PROGRAMMING"
l = str.lower()
print(l)

str1 = "Welcome to Python programming"
u = str1.upper()
print(u)

str2 = "my name is tony stark"
t = str2.title()
print(t)
 
str3 = "mY NAME IS TONY STARK"
c = str3.capitalize()
print(c) 
print()
# find()
# index()
# isalpha()
# isdigit()
# isalnum()

s = "Welcome"
print(s.find('e'))
print(s.find('e',3))
print(s.find('z'))     # returns index value -1
print()

print(s.index('e'))
print(s.index('e',3))
# print(s.index('z'))     shows error
print()

s1 = "Welcome1234"
print(s1.isalpha())   # False
print(s1.isdigit())   # False
print(s1.isalnum())   # True  it returns false when there is a special character is exist in string
print()

# chr()
# ord()

y = chr(65)
print(type(y) , y)
a = ord('A');
print(type(a) , a)
print()

# String format() method

# Three ways to format our strings  

# 1. Named indexes
s = "Welcome to {fname} {lname}".format(fname = "Python" , lname = "Programming")
print(s)
s = "Welcome {a} to {b} programming".format(a = 50 , b = 20)
print(s)
s = "Welcome {a:10} to {b} programming".format(a = 50 , b = 20)       # >  = --------50
print(s)
s = "Welcome {a:^10} to {b} programming".format(a = 50 , b = 20)      # ^  = ----50----
print(s)
s = "Welcome {a:<10} to {b} programming".format(a = 50 , b = 20)      # <  = 50--------
print(s)

print()

# 2. Numbered indexes
s = "Welcome {0} to {1} {2}".format("WSCube","Tech","Python")
print(s)
s = "Welcome {1} to {2} {0}".format("WSCube","Tech","Python")
print(s)

print()

# 3. Empty palceholders
s = "{} to {} Welcome {}".format("WSCube","Tech","to")
print(s)
s = "{} to {} Welcome {}".format("WSCube","Tech","to")
print(s)

