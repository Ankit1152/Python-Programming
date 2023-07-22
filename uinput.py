# whenever we take input from the user it comes as a string
a = input("Enter the value of a :")             # 10
b = input("Enter the value of b :")             # 20
print(a + b)                            # Output  1020  


# So We need to typecaste the user input into desired datatype
a = int(input("Enter the value of a :"))        # 10 
b = int(input("Enter the value of b :"))        # 20 
print(a + b)                             # Output 30   


a = float(input("Enter the value of a :"))      # 10.5
b = float(input("Enter the value of b :"))      # 25
print(a + b)                            # Output  35.5


a = eval(input('Enter the value of a :'))       # 0b1000
b = eval(input('Enter the value of b :'))       # 10.5
c = eval(input('Enter the value of c :'))       # 20
print(a + b + c)                        # Output  38.5