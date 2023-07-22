d = {
    'Name':'python',
    'Fees':2000,
    'Duration':'2 Months'
}
print(type(d), d)

# Get the element in the Dictionary one by one
print(d['Fees'])      
print(d['Duration'])
print(d['Name'])

# Iterating Dictionary elements using for loop

for n in d:
    print(n)           # It prints only Keys 
    print(d[n])        # It prints keys with values

