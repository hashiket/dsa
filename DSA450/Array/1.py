#reverse the array

lst = [1,2,3,4,5]

#print(lst[::-1])
start=0
end=len(lst)-1
while start< end:
    lst[start],lst[end]=lst[end],lst[start]
    start+=1
    end-=1
print(lst)
