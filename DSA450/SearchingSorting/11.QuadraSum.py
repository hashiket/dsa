#find four elements that sum to a given value
#O(n^4)
# def quadra(arr,key):
#     n=len(arr)
#     for i in range(n-3):
        
#         for j in range(i+1,n-2):
#             for k in range(j+1,n-1):
#                 for l in range(k+1,n):
#                     #print( arr[i]+arr[j]+arr[k]+arr[l])
#                     if (arr[i]+arr[j]+arr[k]+arr[l])==key:
                        
#                         print( f"{arr[i]},{arr[j]},{arr[k]},{arr[l]}")



#O(n^3)
# def quadra(arr, k):
#     n=len(arr)
#     for i in range(n-2):
#         for j in range(i+1,n-1):
           
#             l=j+1
#             r=n-1
#             while l<r:
#                 if arr[i]+arr[j]+arr[l]+arr[r]==k:
#                     print(arr[i],arr[j],arr[l],arr[r])
#                     l+=1
#                     r-=1
#                 elif arr[i]+arr[j]+arr[l]+arr[r]<k:
#                     l+=1
#                 else:
#                     r-=1





arr=[10,2,3,4,5,7,8]

quadra(arr,23)


