#check whether string is palidrome or not 

def palidrome(str1):

    return str1==str1[::-1]

str1="absdba"

print(palidrome(str1))
