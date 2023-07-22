n = int(input("Enetr a number: "))
reverse = 0
  
# Condition may also be like n % 10 != 0
while n > 0:
    lastdigit = n % 10
    reverse = reverse * 10 + lastdigit
    n = n // 10

print(reverse)    
