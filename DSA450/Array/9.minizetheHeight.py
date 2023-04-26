def minh(arr,k):
    n=len(arr)
    arr.sort()
    ans = arr[-1]-arr[0]
    for i in range(1,n):
        if arr[i]-k<0:continue

        max_ = max(arr[i-1]+k,arr[-1]-k)
        min_ = min(arr[i]-k,arr[0]+k) 

        ans = min(ans,max_-min_)

    return ans

arr = [1, 5, 8, 10]
k=2
print(minh(arr,k))