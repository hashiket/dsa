#Find the element in sorted and rotated array

def sorted(arr, target):
    n=len(arr)
    s,e=0,n-1
    mid = (s+e)//2
    while s<=e:
        mid = (s+e)//2
        if target==arr[mid]:
            return mid
        if arr[s]<=arr[mid]:
            if arr[s]<=target and arr[mid]>=target:
                e=mid-1
            else:
                s=mid+1
        else:
            if arr[e]>=target and arr[mid]<=target:
                s=mid+1
            else:
                e=mid-1

    return -1

arr=[4,5,6,7,0,1,2]
print(sorted(arr, 0))