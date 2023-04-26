def search(lst,n,x):
    for i in range(0,n):
        if (lst[i]==x):
            return i
    return -1

lst=[1,2,3,4,5,68]

m=search(lst,len(lst),5)
print(-1)
if m==-1:
    print("Element is not found")
else:
    print(f"Element is at {m} index ")