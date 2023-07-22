l = []
while True:
    c = int(input('''
        Enter your choice you want : 
        1 . Push elements
        2 . Pop element
        3 . Peek element
        4 . Display the List elements
        5 . Exit
    '''))

    if c==1:
        n = input("Enter the value:-")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("Stack underflow.....")
        else:
            p=l.pop()
            print(p)
            print(l)

    elif c==3:
        if len(l)==0:
            print("Stack underflow.....")
        else:
            print("Last stack element is: ",l[-1])

    elif c==4:
        print("Elements in the List is: ",l)

    elif c==5:
        break;

    else:
        print("Invalid Operation.....")    


            







