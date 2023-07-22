import random
n = random.randint(3,10)
print(n)
n1 = random.randrange(3,10)
print(n1)

l = [10,20,30,40]
lc = random.choice(l)
print(lc)

# It shuffles the list elements
random.shuffle(l) 
print(l)

# Generates random no between 0 & 1
a = random.random()
print(a)

# It returns floating value between the parameters
u = random.uniform(3,10)
print(u)