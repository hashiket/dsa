#1.Solution 
##??????????????
# def nextPer(arr):
#     idx=-1
#     n= len(arr)-1

#     for i in range(n,-1,-1):
#         if arr[i]>arr[i-1]:
#             idx = idx
#             break
#     if idx == -1:
#         return arr[::-1]
#     else:
#         prev = idx
#         for i in range(idx+1,n):
#             if arr[i]>arr[idx-1] and arr[i]<=arr[prev]:
#                 prev = i

#         arr[idx-1],arr[prev]=arr[prev],arr[idx-1]
#         arr[idx:n-1:-1]

# arr = [1,2,3]
# nextPer(arr)
# print(arr)


#2.Soution

def nextPer(arr):
    n=len(arr)
    k,l=n-2,n-1
    while k>0 and arr[k]>arr[k+1]:
        k-=1
    if k<0:
        arr.reverse()
    else:
        while l>k and arr[l]<=arr[k]:
            l-=1
        arr[k],arr[l]=arr[l],arr[k]
        arr[k + 1:n] = reversed(arr[k + 1:n])

arr = [1,2,3]
nextPer(arr)
print(arr)