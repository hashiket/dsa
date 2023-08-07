#comman Element in three array


def ar(arr1,arr2,arr3):
    return list(set(arr1)&set(arr2)&set(arr3))

arr1=[1, 5, 10, 20, 40, 80]
arr2=[6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(ar(arr1,arr2,arr3))