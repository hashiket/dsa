#move all negative to one side

#solution1
# def sort(arr):
#     s=0
#     e=len(arr)-1

#     while(s<e):
#         if arr[s]<0:
#             s+=1

#         elif arr[e]>0:
#             e-=1
#         else:
#             arr[s],arr[e]=arr[e],arr[s]



#solution2


def sort(arr):
    j=0
    for i in range(len(arr)-1):
        if arr[i]<0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1

arr = [1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]
sort(arr)
print(arr)






