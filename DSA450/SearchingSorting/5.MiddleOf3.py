def middle(a,b,c):
    maxx = max(a,max(b,c))
    minn = min(a,min(b,c))
    m = a+b+c - (maxx+minn)
    return m

print(middle(5,3,8))