m=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
while i<len(m):
    list_mark=m[i]
    length=len(list_mark)
    j=0
    a=0
    s=0
    while j<len(list_mark):
       s=s+m[i][j]
       a=s//length
       j=j+1
    i=i+1
    print(a)


 