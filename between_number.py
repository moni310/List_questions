list=[3,10,17]
i=0
empty_list=[ ]
while i<len(list):
    j=list[i]
    while j<=list[-1]:
        k=j
        empty_list.append(k)
        j=j+1
    i=i+1
print(empty_list)