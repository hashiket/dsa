#1.Solution

# def sellStock(arr):
#     cp = 0
#     mp=0

#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#             cp=arr[j]-arr[i]
#             if cp>mp:
#                 mp=cp
#     print( mp)





# arr = [7,1,5,3,6,4]
# sellStock(arr)



def sellStock(arr):
    left=0
    right=1
    max_profit = 0

    while right<len(arr):
        cp = arr[right]-arr[left]
        if arr[left]<arr[right]:
            max_profit = max(cp,max_profit)
        else:
            left=right
        right+=1

    print(max_profit)

arr = [7,1,5,3,6,4]
sellStock(arr)

