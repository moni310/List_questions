num=int(input("enter the number="))
i=0
empty=[ ]
sum=0
while i<num:
    number=int(input("enter the number="))
    empty.append(number)
    k=empty
    sum=sum+k[i]
    i=i+1
print(sum)