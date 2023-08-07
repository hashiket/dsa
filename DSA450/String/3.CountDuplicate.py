#Count number of duplicates in string

def count(str):
    d={}
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in d:
        if d[i]>1:
            print(f"{i} having count {d[i]}")
str="Hello World"

count(str)