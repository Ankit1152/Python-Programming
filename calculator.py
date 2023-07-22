print('''

   '+' Addition
   '-' Subtraction
   '*' Multiplication
   '/' Division
   
''')

num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
opr = input("Enter the operator you want to calculate:")

if opr=='+':
    print(num1 + num2)

elif opr=='-':
    print(num1 - num2)

elif opr=='*':
    print(num1 * num2)

elif opr=='/':
    print(num1 / num2)      

else:
    print("Invalid operator....")      



