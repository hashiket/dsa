def minJumps( arr, n):
    i = 0
    c = 0
    while n>0:
        n=n-arr[i]
        i=arr[arr[i]]
        c+=1
    return c

arr = [1,3,5,8,9,2,6,7,6,8,9]
n=len(arr)-1
print(minJumps(arr,n))
