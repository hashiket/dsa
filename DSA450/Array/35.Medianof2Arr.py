#FInd the median of two array

def median(arr, arr1):
    arr.extend(arr1)

    arr.sort()
    n=len(arr)
    if n%2==0:
        return arr[n//2-1]+arr[n//2]
    else:
        return arr[n//2]

arr1 = [ -5, 3, 6, 12, 15 ]
arr = [ -12, -10, -6, -3, 4, 10 ]
print(median(arr, arr1))