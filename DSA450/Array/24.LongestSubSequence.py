#Find the Longest SubSequence in array i.e 1,2,3,4,5

def longSeq(arr):
    numSet = set(arr)
    longest=0
    for i in range(len(arr)):
        if (arr[i]-1) not in numSet:
            maxl=0
            while ((arr[i]+maxl) in numSet):
                maxl+=1
            longest = max(longest, maxl)

    return longest


arr=[2,6,1,9,4,5,3]
print(longSeq(arr))
