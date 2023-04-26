#Merge the two sorted array using extra space

# def  merge(arr1,arr2):
#     i=j=k=0
#     arr=[None]*(len(arr1)+len(arr2))
#     while (i<len(arr1) and j<len(arr2)):

#         if arr1[i]<arr2[j]:
#             arr[k]=arr1[i]
#             i+=1
#         else:
#             arr[k]=arr2[j]
#             j+=1
#         k+=1

#     while i < len(arr1):
#         arr[k]=arr[i]
#         i+=1
#         k+=1
#     while j < len(arr2):
#         arr[k]=arr[j]
#         j+=1
#         k+=1


#     return arr


#without using extra space
#dump

# def merge(arr1,arr2):
#     n=len(arr1)
#     m=len(arr2)

#     while n>0 and m>0:
#         if arr1[n-1]>=arr2[m-1]:
#             arr2[n+m-1]=arr1[n-1]
#             m-=1
#         else:
#             arr1[n+m-1]=arr2[m-1]
#             n-=1
#     if n>0:
#         arr1[:n]=arr2[:n]

#     return arr1
# arr1=[2,3,5,7,9]
# arr2=[4,6,8,1]

# print(merge(arr1,arr2))

