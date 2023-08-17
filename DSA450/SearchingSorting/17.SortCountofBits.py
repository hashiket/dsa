#Sort array according to count of set bits

def sortBySetBitCount( arr, n):
    a={}

    for i in arr:
        b = bin(i).replace("0b","")
        c= b.count("1")

        if c in a:
            a[c].append(i)
        else:
            a[c]=[i]
        
    #print("a", a)
    s=sorted(a.items(), key = lambda x: x[0])[::-1]
        #s=sorted(a.items(),key=lambda x: x[0])[::-1]
    #print("s",s)
    ans = []

    for i in s:
        ans.extend(i[1])
    #print("ans",ans)
           
    for i in range(len(arr)):
        arr[i]=ans[i]

arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
sortBySetBitCount(arr, len(arr))

print(arr)