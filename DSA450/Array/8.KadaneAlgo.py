#Kadane's Algorithm
#find the largest sum of contigous subarray
#1.solution O(N)complexity
# def maxSubArray(arr):
#     n=len(arr)
#     maxSum=arr[0]
#     curSum=0

#     for i in range(n):
#         curSum+=arr[i]

#       if curSum>maxSum:
#         maxSum=curSum
        # if curSum<0:
        #         curSum=0

#     return maxSum

#2.Solution with O(N**2)
def maxSubArray(arr):
    n=len(arr)
    maxSum=arr[0]
    for i in range(n):
        currSum=0
        for j in range(i,n):
            currSum+=arr[j]
        if currSum>maxSum:
            maxSum=currSum
    return maxSum

arr = [2,3,-4,5,6,-1]

print(maxSubArray(arr))
