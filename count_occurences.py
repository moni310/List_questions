list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x"]
i=0
b=[ ]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
a=b
j=0
p=[ ]
while j<len(a):
    k=0
    count=0
    d=[ ]
    while k<len(list):
        if b[j]==list[k]:
            count=count+1
        k=k+1
    d.append(b[j])
    d.append(count)
    p.append(d)
    j=j+1
    print(list[j],count)
print(p)







