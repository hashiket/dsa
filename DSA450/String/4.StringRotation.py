#find string is equal to the rotation another string.
#**************************************************************************
def rotateArray(st1,st2):
    if len(st1)!=len(st2):
        return 0

    temp = st1 + st2
 
    if (temp.count(st2) > 0):
        return 1
    else:
        return 0

st1 = "AACD"
st2 = "ABDA"

print(rotateArray(st1,st2))
#****************************************************************************