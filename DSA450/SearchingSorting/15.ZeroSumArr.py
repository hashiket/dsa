#Find the Sub array having count zero
from collections import defaultdict
def find(arr):
   
    
    ans = csum = 0
    D = defaultdict(int)
    D[0] = 1
    for i in arr:
        csum += i
        ans += D[csum]
        D[csum] += 1
    return ans
   

arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
print(find(arr))
