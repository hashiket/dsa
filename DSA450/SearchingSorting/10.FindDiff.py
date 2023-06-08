#find a pair with a given difference

# def pair(arr, d):
#     arr.sort()
#     s=0
#     e=0
#     while e<len(arr)-1:
#         if (arr[e]-arr[s])==d:
#             return arr[s],arr[e]

#         elif arr[e]-arr[s]<d:
#             e=-1
#         else:
#             s+=1
#     return -1


def pair(arr, d):
    arr.sort()
    for i in range(len(arr)):
        e=d+arr[i]
        arr1=arr[i+1:]
        if e in arr1:
            return arr[i],e
arr=[5, 20, 3, 2, 5, 80]

print(pair(arr,78))
