#Find the repeating and missing element in array


def find(arr):
    m=max(arr)
    lst=[]
    for i in range(1,m+1):
        if i not in arr:
            lst.append(i)
    d={}
    rpt=[]
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in d:
        if d[i]>1:
            rpt.append(i)


    return lst, rpt

    


arr=[2,2]
print(find(arr))