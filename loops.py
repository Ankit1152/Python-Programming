print("***********For loop in Python***********")
for x in range(5):        # range(condition)
	print(x)
print()

for x in range(1,6):      # range(starting,condition)
    print(x)
print()

for x in range(1,6,2):    # range(starting,condition,updation) 
    print(x)    
print()

for x in range(5):
	print("Welcome")



print("*******Table of 2 using for loop***********")
for x in range(1,11):
	print("2 *",x ,"=" ,2*x)


# Reverse case....
print('**************Reverse case*****************')
for x in range(10,0,-1):
 	print(x)
print()

for x in range(10,3,-2):
    print(x)	
print()    

for x in range(10,-1,-2):
	print(x)


print("***************While loop*******************")
# Starting
# Condition
# increment/decrement

i = 1
while i<=10:
	print(i,"While Loop")
	i+=1
print(i)

print()

a = 10
while a>=1:
	print(a,"Python")
	a-=1
print(a)

