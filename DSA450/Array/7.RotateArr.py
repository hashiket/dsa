#Rotate array by one in clockwise
#1.Solution
# def rotate(arr):
#     n=len(arr)
#     a=[]
#     b=[]
#     for i in range(n-1,n):
#         a.append(arr[i])
        
#     for j in range(0,n-1):
#         b.append(arr[j])
        
#     j=0
#     for i in range(len(a)):
#         arr[j]=a[i]
#         j+=1
#     for i in range(len(b)):
#         arr[j]=b[i]
#         j+=1  

#2.Solution
def rotate(arr):
    n=len(arr)
    t=arr[0]
    p=0
    for i in range(1,n):
        p=arr[i]
        arr[i]=t
        t=p
    arr[0]=t
      
arr=[1,2,3,4,5]
rotate(arr)
print(arr)