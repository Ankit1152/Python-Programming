course = {
    'php':{'Duration':'2 Months','Fees':10000},
    'java':{'Duration':'3 Months','Fees':15000},
    'python':{'Duration':'5 Months','Fees':12000}
}

print(course)
print(course['python'])
print(course['python']['Fees'])

print()

for k,v in course.items():
    print(k,v)

print()    
course['java']['Fees'] = 50000
for k,v in course.items():
    print(k,v['Duration'], v['Fees'])
    

 