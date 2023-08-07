#Find the first and Last occurence of the element

def occurence(arr, key):
    firstOcc = 0
    c=0
    for i in range(len(arr)):
        if arr[i]==key:
            if firstOcc<=0:
                firstOcc=i 
            c+=1
            
    return f"first {firstOcc} last {firstOcc+c-1}"


arr=[1, 3, 5, 5, 5, 5, 7, 123, 125]
print(occurence(arr, 5))