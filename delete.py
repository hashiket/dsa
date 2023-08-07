<<<<<<< HEAD
def partition(arr, s, e):
    pivot_index = s
    pivot = arr[pivot_index]

    while s<e:
        while s<len(arr) and arr[s]<=pivot:
            s+=1

        while arr[e]>pivot:
            e-=1

        if s<e:
            arr[s],arr[e]=arr[e],arr[s]

    arr[pivot_index],arr[e]=arr[e],arr[pivot_index]
    return e


def quickSort(arr, s, e):
    if s<e:
        p = partition(arr, s, e)
        quickSort(arr, s, p-1)
        quickSort(arr, p+1, e)

arr = [90,89,7,56,34,2,32,10]

quickSort(arr, 0, len(arr)-1)
print("Sorted array:"+str(arr))
=======
>>>>>>> new
