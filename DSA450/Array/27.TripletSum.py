#Triplet is equal to given sum



def findTriplet(arr,target):
    arr.sort()
    c=0
    n=len(arr)
    for i in range(n):
        start=i+1
        end=n-1
        while start<end:
            if(arr[i]+arr[start]+arr[end])==target:
                return 1
            elif (arr[i]+arr[start]+arr[end]>target):
                end-=1
            else:
                start+=1

        return 0


arr=[1,2,4,3,6]
print(findTriplet(arr, 10))


