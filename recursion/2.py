# def fun(n):
#     if n==1:
#         return 0
#     else:
#         return 1+fun(n//2)

# print(fun(16))

# def fun1(n):
#     if n>1:
#         fun1(n-1)

#     for i in range(n):
#         print("*", end="")
#     print()

# fun1(5)
# LIMIT=1000
# def fun2(n):
#     if n<=0:
#         return
#     if n>LIMIT:
#         return
#     print(n, end=" ")
#     fun2(2*n)
#     print(n, end=" ")
# fun2(100)

# def fun(x):
#     if x>0:
#         x-=1
#         fun(x)
#         print(x, end=" ")
#         x-=1
#         fun(x)
# a = 4
# fun(a)

def fun(arr, n):
    if n==1:
        return arr[0]

    else:
        x = fun(arr, n-1)

    if x>arr[n-1]:
        return x

    else:
        return arr[n-1]


arr=[10,20,30,40,45,35]

print(fun(arr, len(arr)))


