def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[89,45,12,45,12,67,89]
bubbleSort(arr)
print(arr)