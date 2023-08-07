#Find a Fixed Point (Value equal to index) in a given array

def find(arr):
    c=[]
    n=len(arr)
    for i in range(n):
        if i in arr:
            c.append(i)

    return c


arr=[15, 2, 45, 12, 7]
print(find(arr))
        