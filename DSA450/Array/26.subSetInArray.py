#Find the subSet between two Array.

#ansW
#**************************************
# def subSet(arr,arr1):
#     m={}
#     n={}
#     for i in arr:
#         if i in m:
#             m[i]=m[i]+1
#         else:
#             m[i]=1

#     for i in arr1:
#         if i in n:
#             n[i]=n[i]+1
#         else:
#             n[i]=1
#     l=len(n)
#     print(m,n)
#     for i in m:
#         if l>0:
#             if i in n:
#                 if m[i]==n[i]:
#                     l-=1
#                 else:
#                     return False
#         else:
#             return True
#******************************************


def subSet(arr,arr1):
    for i in arr1:
        if i in arr:
            arr.remove(i)
        else:
            return False
    return True



                
arr=[11, 7, 1, 13, 21, 3, 7, 3]
arr1=[11, 3, 7, 1, 7]

print(subSet(arr, arr1))