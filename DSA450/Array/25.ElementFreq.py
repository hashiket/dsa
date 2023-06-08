#find the elements with give or more than that frequency 

def eleFreq(arr, k):
    m={}
    lst = []
    key=len(arr)//k
    for i in arr:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1

    for i in m:
        if m[i]> key:
            lst.append(i)

    return lst

arr = [3, 1, 2, 2, 1, 2, 3, 3]
print(eleFreq(arr, 4))
            