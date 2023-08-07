#Find the maximum Product of the sub Array

def subArray(arr):
    curr = 1
    max=0
    for i in arr:
        curr*=i
        if curr>max:
            max=curr
    return max

#arr = [6, -3, -10, 0, 2]
arr = [2, 3, 4, 5, -1, 0]
print(subArray(arr))



# def maxProduct(self,arr, n):
# 		# code here
# 		res = max(arr)
# 	    curr_min , curr_max = 1,1
		 
# 		for i in arr:
# 		    if i ==0:
# 		        curr_min, curr_max = 1,1
# 	        tmp = curr_max*i
# 		    curr_max = max(i,curr_max*i,curr_min*i)
# 		    curr_min = min(i,tmp,curr_min*i)
# 		    res = max(res,curr_min,curr_max)
#         return res