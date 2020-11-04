list=[4,7,2,18,9,10,3,8,28]
b=list[0]
i=0
while i<len(list):
    if list[i]<b:
        b=list[i]
    i=i+1
print(b)