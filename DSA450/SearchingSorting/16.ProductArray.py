#Product array puzzele

#O(n^2)
# def product(arr):
#     pro=1
#     lst=[]
#     for i in arr:
#         for j in arr:
#             if i==j:
#                 continue
#             pro*=j
#         lst.append(pro)
#         pro=1
#     return lst


def product(arr):
    lst=[]
    pro=1
    for i in arr:
        if i==0:
            continue
        pro*=i
    for i in arr:
        if i==0:
            lst[i] = 0
        lst.append(pro//i)
    return lst

        

arr =[10, 3, 5, 6, 2]
print(product(arr))

