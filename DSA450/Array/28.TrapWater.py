#Traping Rain Water in block which is not mention
def trapWater(arr):
    res = 0
    n=len(arr)
    lmax = [0]*n
    rmax = [0]*n
    lmax[0] = arr[0]
    for i in range(1,n):
        lmax[i] = max(arr[i],lmax[i-1])
        rmax[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        rmax[i]=max(arr[i],rmax[i+1])
    for i in range(1,n-1):
        res+= min(lmax[i],rmax[i])-arr[i]
    return res    


arr=[3,0,0,2,0,4]
print(trapWater(arr))       