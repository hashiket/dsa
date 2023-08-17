#K-th Element of Two Sorted Arrays

def find(arr1, arr2,key):
    i=j=k=0
    arr = [None]*(len(arr1)+len(arr2))
    while i < len(arr1) and j < len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1

    while i< len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1

    while j<len(arr2):
        arr[k]=arr2[j]
        k+=1
        j+=1

    print(arr)

    for i in range(1,len(arr)):
        if i==key:
            return arr[i-1]

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]

print(find(arr1, arr2, 5))