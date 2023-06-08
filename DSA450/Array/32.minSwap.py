#Minimum swaps required bring elements less equal K together

def minSwap(arr, k):
    n=len(arr)
    c=0
    for i in arr:
        if i<=k:
            c+=1
    if c==0:
        return 0

    left,right,bad=0,0,0
    ans=999999999999999999
    while(right<=n-1):
        if arr[right]>k:
            bad+=1

        if right-left+1<c:
            right+=1
            continue

        if right-left+1==c:
            ans=min(ans, bad)

            if arr[left]>k:
                bad-=1
            left+=1
            right+=1
    return ans


arr=[2, 1, 5, 6, 3]
print(minSwap(arr, 3))