# lst=[]
# lst1=[]
# lst2=[]
arr = [2,0,1,1,0,0,2,1]  
# for i in arr:
#     if i==0:
#         lst.append(i)
#     elif i==1:
#         lst1.append(i)
        
#     elif i==2:
#         lst2.append(i)
        
# lst.extend(lst1)
# lst.extend(lst2)
# print(lst)

one=two=zero=0
for i in arr:
            if arr[i]==0:
                zero+=1
            elif arr[i]==1:
                one+=1
            elif arr[i]==2:
                two+=1
                
j=0
for i in range(zero):
            arr[j]=0
            j+=1
            
for i in range(one):
            arr[j]=1
            j+=1
for i in range(two):
            
                arr[j]=2
                j+=1

print(arr)