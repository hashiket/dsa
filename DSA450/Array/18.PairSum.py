#Count pairs with given sum

# def sump(arr, key):
#     c=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if (arr[j]+arr[i])==key:
#                 c+=1

#     return c

# arr =[1, 1, 1, 1]
# print(sump(arr, 2))


def sump(arr, key):
    m = {}
    ans=0
    for i in arr:
        b = key-arr[i]
        if b in m:
            ans = ans + m[b]
        if i in m:
            m[i] = m[i]+1
        else:
            m[i]=1

    return ans

arr =[1, 1, 1, 1]
print(sump(arr, 2))
