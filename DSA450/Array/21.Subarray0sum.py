#Find subarray equals to 0

def subArray(arr):
    if 0 in arr:
        return True
    else:
        if sum(arr)==0:
            return True
        else:
            curr=0
            d={}
            for ele in arr:
                curr=curr+ele

                if curr==0:
                    return True
                else:
                    if ele in d:
                        return True
                    else:
                        d[curr]=0
            return False

arr=[4,2,-3,1,6]
print(subArray(arr))

    
                    
