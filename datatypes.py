from typing import List


print("**********Numeric Datatypes***********")

# 1. integers
# 2. float
# 3. Complex numbers

a = 10                                         # Numeric Datatypes
print(a , type(a))

a = 5.10
print(a , type(a))

a = 5 + 2j
print(a , type(a))

print("***********Sequence Datatypes************")

# 1. String
# 2. List
# 3. Tuples

s = 'Hello@1234'         # String Datatypes
print(s , type(s))
s = "I am learning Python programming language"
print(s , type(s))

s = '''

   Hello@1234
   I am learning Python Programming language

'''
print(s , type(s))

# List Datatypes and it is Mutable 

l = [10 , 20 , 'Python' , 'C++']               
print(l[2])
l[2] = 'java'                
print(l , type(l))

# Tuples Datatypes   Immutable datatypes 

t = (10 , 20 , "Rodrigo", 1 + 2j)           
print(t , type(t))


print("**************Dictionary Datatypes***************")

d = {                                           # Mutable Datatypes
	'course_name' : 'Python' ,
	'course_duration' : '2 Months'
}

print(d['course_name'])
print(d , type(d))

print("*******************Set Datatypes******************")

my_set = {10 , 20 , 30 , 10}                    #Immutable Datatypes
print(my_set , type(my_set))