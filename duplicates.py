num=[12,45,12,45,32,87,67,98,45,67,34,12,23,65]
i=0
empty=[ ]
while i<len(num):
    if num[i] not in empty:
        empty.append(num[i])
    i=i+1
print(empty)