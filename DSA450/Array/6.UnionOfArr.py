
#set(a+b)

def un(a,b):
    c=[]
    for i in a:
            if  i  not in c:
                c.append(i)
    for i in b:
            if i not in c:
                c.append(i)
    print(len(c))
    print(c)


a=[1,2,3,4,5]
b=[1,2,3]

un(a, b)