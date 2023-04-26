def findDuplicate(arr):
    s = set()

    for i in arr:
        if i in s:
            return i
        else:
            s.add(i)

arr = [2,3,4,4]
print(findDuplicate(arr))