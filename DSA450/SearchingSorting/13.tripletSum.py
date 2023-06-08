#Count triplets with sum smaller than X

def triplet(arr, k):
    sum=0
    for i in range(len(arr)):
        ans=arr[i]
        l=i+1
        r=len(arr)-1
        while l<r:
            if ans+arr[l]+arr[r]<k:
                return arr[i],arr[l],arr[k]
            elif ans+arr[l]+arr[k]>k:
                r-=1
            else:
                l+=1
        
    return -1


arr=[-2, 0, 1, 3]
print(triplet(arr, 2))