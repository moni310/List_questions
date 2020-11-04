list=[3,5,6,7,1,9,5]
list1=[4,2,5,6,7,9,3]
i=0
sum=0
b=[]
while i<len(list):
    sum=sum+list[i]+list1[i]
    i=i+1
    b.append(sum)
print(b)
print(sum)
