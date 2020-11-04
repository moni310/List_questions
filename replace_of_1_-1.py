list=[1,5,7,1,9,4,1,6,1,0]
i=0
b=[ ]
while i<len(list):
    if list[i]==1:
        a=list[i]*-1
        b.append(a)
    else:
        b.append(list[i])
    i=i+1
print(b)
