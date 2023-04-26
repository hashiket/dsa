

a = [64,4678,90,12,90,12]

for i in range(len(a)):
    mid_idx = i 
    for j in range(i+1,len(a)):
        if a[mid_idx]>a[j]:
            mid_idx=j
    a[i],a[mid_idx]=a[mid_idx],a[i]

print("Sorted array")

print(a)