#Stickler the thief wants to loot money from a society having n houses in a single line. 
# He is a weird person and follows a certain rule when looting the houses. According to the rule, 
# he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. 
# The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
#  He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i]amount of money present in it.


def collection(arr):
    n=len(arr)
    a1=0
    a2=0
    for i in range(n):
        if i%2==0:
            a1+=arr[i]
        else:
            a2+=arr[i]

    return max(a1,a2)

#arr=[5,5,10,100,10,5]
arr=[1,2,3]
print(collection(arr))