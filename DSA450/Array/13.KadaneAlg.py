def ka(arr):
    currSum=0
    Maxsum=arr[0]

    for i in range(len(arr)):
        currSum+=arr[i]

        if currSum>Maxsum:
            Maxsum=currSum

        if currSum<0:
            currSum=0

    return Maxsum

arr = [9,-2,-2,-6,10,-9]

print(ka(arr))
print(1)