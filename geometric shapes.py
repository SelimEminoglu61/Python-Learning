def geometry(shape):
    if len(shape)==3:    # len ile listenin boyu olculur.
        a=shape[0]
        b=shape[1]
        c=shape[2]
        if (a+b)>c and (a+c)>b and (b+c)>a :
            if (a==b)and (a==c) and (b==c):
                print("thıs is rhombus")
            elif (a==b):
                print("this is twinned triangle")
            elif (a==c):
                print("this is twinned triangle")
            elif (b==c):
                print("this is twinned triangle")
            else:
                print("ıt ıs normal triangle")
        else:
            print("ıt ısnt triangle")
    elif len(shape)==4:
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]
        if (a==b)and(a==c)and(a==d):
            print("ıt is square")
        elif (a==c) and (b==d):
            print("it is rectangular")
        else:
            print("ıt ıs normal rectangular")
    else:
        print("there ısnt any shape")


while (True):
    member_number=int(input("give your member number:"))
    if (member_number==3):
        a = int(input("first value:\n"))
        b = int(input("second value:\n"))
        c = int(input("third value:\n"))
        serie=[a,b,c]
        geometry(serie)
    elif(member_number==4):
        a = int(input("first value:\n"))
        b = int(input("second value:\n"))
        c = int(input("third value:\n"))
        d = int(input("fourth value:\n"))
        serie2=[a,b,c,d]
        geometry(serie2)
    else:
        print("please type again")
