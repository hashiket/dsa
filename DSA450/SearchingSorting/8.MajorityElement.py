#find majority element

def majority(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=0
    for i in d:
        if d[i]>len(arr)//2:
            ans=max(ans,d[i])
    return ans

arr=[3,1,3,3,2]
arr=[1,3,2]
print(majority(arr))