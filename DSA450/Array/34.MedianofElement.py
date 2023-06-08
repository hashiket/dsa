#Median of the element

def median(arr):
    n=len(arr)
    arr.sort()
    if n%2==0:
        return (arr[n//2-1]+arr[(n//2)])//2
    else:
        return arr[(n//2)]


arr=[90,100,78,89,67]
#arr=[56,67,30,79]
print(median(arr))