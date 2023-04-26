def shellSort(arr):
    gap=len(arr)//2
    while gap>0:
        i=0
        j=gap

        while j<len(arr):
            if arr[i]>arrj[j]:
                arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1

            k=1
            while k-gap>-1:
                if arr[k-gap]>arr[k]:
                    arr[k-gap],arr[k]=arr[k],arr[k-gap]
                k-=1

        gap//=2

arr = [67,89,12,76,54,12,7,23]
shellSort(arr)
print(arr)
