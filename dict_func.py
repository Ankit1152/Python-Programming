# 1 . get()
# 2 . keys()
# 3 . values()
# 4 . items()

d = {
    'Name':'Python',
    'fees':8000,
    'Duration':'2 months',
    'Program':'MCA',
}

n = d.get('fees')
print(n)


for a in d.keys():
    print(a)

for a in d.values():
    print(a)    

for a,b in d.items():
    print(a,b)

print()

# 5 . del
# 6 . pop()
# 7 . dict()
# 8. update()
# 9 . clear()


del d['Program']
print(d)                      #  {'Name': 'Python', 'fees': 8000, 'Duration': '2 months'}

p = d.pop('fees')
print(d , p)                  #  {'Name': 'Python', 'Duration': '2 months'} 8000

d = dict(name = 'Java' , duration = '3 Months' , Program = 'MCA')
print(d)                      #  {'name': 'Java', 'duration': '3 Months', 'Program': 'MCA'}  

d.update({'duration':'5 Months' , 'Program':'B.Tech'})
print(d)                      #  {'name': 'Java', 'duration': '5 Months', 'Program': 'B.Tech'}

d.clear()
print(d)                      # {}


print()
# Insert element in the dictionary

d['description'] = 'This is Python course'
d['course'] = "Java"
d['name'] = 'Ankit'
print(d)                     # {'description': 'This is Python course', 'course': 'Java', 'name': 'Ankit'}

d['course'] = "JavaScript"    
print(d)                     #  {'description': 'This is Python course', 'course': 'JavaScript', 'name': 'Ankit'}
