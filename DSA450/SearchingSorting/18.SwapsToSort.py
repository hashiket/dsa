#minimum no. of swaps required to sort the array
from collections import OrderedDict

def minSwaps(nums):
    dic  = OrderedDict()
    for i in range(len(nums)):
        dic[nums[i]] = i

    sorted_dic = OrderedDict(sorted(dic.items()))

    swaps = 0

    for i, v in enumerate(sorted_dic.values()):
        if i!=v:
            nums[i], nums[v] = nums[v], nums[i]
            sorted_dic[nums[i]], sorted_dic[nums[v]] = sorted_dic[nums[v]], sorted_dic[nums[i]]
            swaps+=1
    return swaps

arr = [10, 19, 6, 3, 5]
print(minSwaps(arr))