import sys

def min_index(arr, s, e):
    sml = sys.maxsize
    mindex = 0

    for i in range(s,e):
        if sml>arr[i]:
            sml=arr[i]
            mindex = i

    return mindex

def fun2(arr, start_index, end_index):
    if start_index>=end_index:
        return
    
    mindex = min_index(arr, start_index, end_index)

    arr[start_index],arr[mindex]=arr[mindex],arr[start_index]

    fun2(arr, start_index+1, end_index)

arr=[23,1,23,45,6,7,78,90,67,69]

fun2(arr, 0, len(arr))
print(arr)
