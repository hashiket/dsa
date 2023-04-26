def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergeSort(left_arr)
        mergeSort(right_arr)

        i=j=k=0
        for i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[]