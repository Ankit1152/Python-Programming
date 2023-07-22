l = []

while True:
    c = int(input('''

    1 . Enqueue Operation
    2 . Dequeue Operation
    3 . Front element
    4 . Rear element
    5 . Display Queue elements
    6 . Exit

    '''))

    if c==1:
        n = input("Input the value you want to add :-")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Queue is Empty")
        else:
            del l[0]
            print(l)  
    elif c==3:
        if len(l)==0:
            print("Queue is empty..")
        else:
            print("Front element of the queue:-", l[0])
    elif c==4:
        if len(l)==0:
            print("Queue is empty")
        else:
            print("Rear element of the queue:- ", l[-1]) 
    elif c==5:
        print("Element in the queue :-",l)
    elif c==6:
        break;
    else:
        print("Invalid operation")                                            




