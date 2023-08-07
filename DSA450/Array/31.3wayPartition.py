#Three way partitons 

def partitons(arr, a,b):
    l=[i for i in arr if i<a]
    k=[i for i in arr if i>=a and i<=b]
    m=[i for i in arr if i>b]

    arr.clear()
    arr = l[:] + k[:] + m[:]
    return arr

arr = [1, 2, 3, 3, 4]
print(partitons(arr,1,2))