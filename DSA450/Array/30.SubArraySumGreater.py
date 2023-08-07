#find the smaallest sub array having count greater than given value

# def subArray(arr, k):
#     n=len(arr)
#     ml = n+1

#     for i in range(n):
#         currSum=arr[i]
#         if currSum>k:
#             return 1
#         for j in range(i+1,n):
#             currSum+=arr[j]
#             if currSum>k and (j-1+1)<ml:
#                 ml=(j-i+1)

#     return ml

#BestApprouch

def subArray(arr, k):
    s=e=0
    sum=0
    n=len(arr)
    a=n
    while e<n:
        while e<n and s<=k:
            sum+=arr[e]
            e+=1
        while s>k and s<=e:
            sum-=arr[s]
            s+=1
        a=min(a,e-s+1)
    return a


arr = [1, 4, 45, 6, 0, 19]
print(subArray(arr, 51))