#distribute chocalte with minimum diff bet first and last


def minDiff(arr, m):
    arr.sort()

    n=len(arr)
    l=[]
    for i in range(m):
        l.append(arr[i])

    mn=abs(l[0]-l[-1])
    j=0
    for i in range(m,n):
        l.pop(j)
        l.append(arr[i])
        mn=min(mn,abs(l[0]-l[-1]))
    return mn

arr=[3, 4, 1, 9, 56, 7, 9, 12]

print(minDiff(arr, 5))