#Searching in an array where adjacent differ by at most k
#**********************************************S
def diff(arr,k,e):
    n=len(arr)
    i=0
    while i<n:
        if arr[i]==e:
            return i 

        i=i+max(1,int(abs(arr[i]-e)//k))
    return -1

arr=[4, 5, 6, 7, 6]
print(diff(arr,1,5))