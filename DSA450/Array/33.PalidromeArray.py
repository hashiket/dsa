#check array having each element palidrome or not

def palidrome(arr):
    for i in arr:
        if i!=int(str(i)[::-1]):
            return 0
    return 1

#arr=[111,222,333,444,555]
arr=[121,131,20]

print(palidrome(arr))