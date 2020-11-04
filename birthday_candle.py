age=int(input("enter the age"))
i=0
a=[ ]
while i<age:
    candle=int(input("enter the number"))
    a.append(candle)
    i=i+1
b=a
j=0
max1=0
while j<len(b):
    if b[j]>max1:
        max1=b[j]
    j=j+1
count=0
k=0
while k<len(b):
    if b[k]==max1:
        count=count+1
    k=k+1
print(count)