# def merge(arr, left, right, mid):
#     i=j=k=0
#     c=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             arr[k]=arr[i]
#             i+=1
#         else:

#             arr[k]=arr[j]
#             j+=1
#             c+=mid-i
#         k+=1
            
#     while i< len(left):
#         arr[k]=arr[i]
#         i+=1
#         k+=1

#     while j <len(right):
#         arr[k]=arr[j]
#         j+=1
#         k+=1

#     return c



# def mergeSort(arr):
#     c=0
#     if len(arr)>1:   
#         mid=len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]

#         c+=mergeSort(left)
#         c+=mergeSort(right)
#         c+=merge(arr,left,right,mid)

#     return c


# arr = [2, 4, 1, 3, 5]
# print(mergeSort(arr))






def mergeSort( arr, n):
        if n < 2:
            return 0
        mid = n //2
        left = arr[:mid]
        right = arr[mid:]
        c = 0
        
        c += mergeSort(left, mid)
        c += mergeSort(right, n - mid)
        c += merge(arr, left, right, mid, n-mid)
        return c
        
def merge( arr, left, right, mid, n):
        i = 0
        j = 0
        k = 0
        c = 0
        
        while i < mid and j < n:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                c += mid - i
                j += 1
            k += 1
        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return c

arr = [2, 4, 1, 3, 5]
print(mergeSort(arr,5))