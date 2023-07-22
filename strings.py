# Indexing in Strings
print("***********Indexing in Strings************")
s = "Welcome to Python programming"

print(s[0])
print(s[6])
print(s[11])
print(s[-1])
print(s[-4])
print(s[-7])

#Slicing in Strings

print("***********Left to Right Slicing in Strings************")
print(s[0:7])
print(s[0::2])
print(s[0:])

print("***********Right to left Slicing in strings************")
print(s[-1:-10:-2])
print(s[-1::-2])
print(s[-1::-1])   # Reverse a String
print(s[-1:-10:-1])


print("***********Iteration of Strings**************")

l = len(s);
print(l)

for x in range(l):
	print(s[x])

# print("************1st method Reverse Iteration of String************")
# s = s[-1::-1]
# l = len(s)
# print(l)

# for x in range(l):
# 	print(s[x])

print()

for x in range(l-1,-1,-1):
	print(s[x])


print("************Another method to Reverse String without knowing length**************")	

s2 = "My name is Ankit kumar"
s2 = s2[-1::-1]

for x in s2:
	print(x)