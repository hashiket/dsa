def maxSumArray(arr):
    currSum=0
    maxSum = arr[0]

    for i in arr:
        currSum+=i 
        if currSum>maxSum:
            maxSum = currSum
        if currSum<0:
            currSum = 0

    return maxSum

arr = [2,3,-4,5,6,-1]

rt = maxSumArray(arr)

print(rt)

        