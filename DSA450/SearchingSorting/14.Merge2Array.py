#Merge teo sorted array


def Merge(arr,arr1):
    i=j=k=0
    
    n=len(arr)
    m=len(arr1)
    a=[None]*(n+m)
    print(len(a))
    while i<n and j<m:
        if arr[i]<arr1[j]:
            a[k]=arr[i]
            i+=1
        else:
            a[k]=arr1[j]
            j+=1
        k+=1

    while i< n:
        a[k]=arr[i]
        k+=1
        i+=1

    while j<m:
        a[k]=arr1[j]
        k+=1
        j+=1
    return a

arr=[2,4,7,9,12]
arr1=[1,5,8,14]

print(Merge(arr,arr1))
