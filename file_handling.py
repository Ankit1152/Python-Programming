import os

# file_obj = open("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt","w")
# file_obj.write("Hii, my name is Ankit \n I am learning file handling in Python")

# file_obj = open("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt","r")
# print(file_obj.read(100))  
# print(file_obj.readline())
# print(file_obj.readlines())    # readlines() :- It gives the output in the form of list


# try:
#     file_obj = open("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt","r")
#     print(file_obj.readlines())
# except:
#     print("File not exist...Plz create first")
# else:
#     file_obj.close()
#     print("File closed...")


# # Copying one file data to another file
# try:
#     with open("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt") as f2:
#             with open("C:\\Users\\amit\\Desktop\\pyprogram\\file1.txt","w") as f3:
#                 for i in f2:
#                     f3.write(i)
# except:
#     print("File not exist...Plz create first")
# # else:
#     f2.close()
#     print("File closed...")

# #  Delete or remove a file
# if os.path.exists("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt"):
#     os.remove("C:\\Users\\amit\\Desktop\\pyprogram\\file.txt")
#     print("File deleted succesfully")

# else:
#     print("File not exist")



# File threading by Telusko

f = open('my_data','w')
f.write("Hello my name is Ankit")
f = open('my_data','r')
print(f.read())
f = open('my_data','a')
f.write("I am appending the lines")

f1 = open('my_data1','w')
f1.write("Hii i amm learning File handling")

f = open('my_data','r')

for data in f:
    f1.write(data)
