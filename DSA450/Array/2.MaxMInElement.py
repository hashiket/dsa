#Fint the Maximum and Minimum element in array

lst = [10,23,34,56,67,9,80,45]


max=0
min=lst[0]

for i in range(len(lst)):
    if lst[i]<min:
        min=lst[i]

    if lst[i]>max:
        max=lst[i]

print("Minimum",min)
print("Maximum", max)